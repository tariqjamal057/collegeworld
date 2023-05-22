from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from college.forms import NewsLetterForm, AddEducation, AddProfile
from django.http import JsonResponse
from college.models import College, CollegeStream, CollegeDegree, CollegeQuestion, CounsellingData
from django.core.paginator import Paginator
from django.db.models import Q
from college.models import UserDetail, Degree, Education
from django.template.loader import render_to_string
from django.forms.models import model_to_dict


# Create your views here.
@login_required(login_url = 'login')
def home(request):
    context = {
        "newsletter": NewsLetterForm()
    }
    return render(request, 'college/home.html', context)

@login_required(login_url = 'login')
def college(request):
    if 'search_college' in request.GET:
        search_college=request.GET['search_college']
        colleges=College.objects.filter(Q(name__icontains=search_college) | Q(city__icontains=search_college) | Q(state__icontains=search_college))
    else:
        colleges = College.objects.all()
        search_college = None
    paginator=Paginator(colleges,3)
    page_num=request.GET.get('page',1)
    colleges=paginator.page(page_num)

    # Recommendation code 
    #  location = request.POST.get('location')
    #  size = request.POST.get('size')
    #  program = request.POST.get('program')
    #  culture = request.POST.get('culture')
       
    #     # Get all colleges and their features
    #     colleges = College.objects.all()
    #     college_features = []
    #     for college in colleges:
    #         features = college.location + ' ' + college.size + ' ' + college.programs + ' ' + college.culture
    #         college_features.append(features)
       
    #     # Compute content-based recommendations
    #     tfidf_vectorizer = TfidfVectorizer()
    #     college_tfidf = tfidf_vectorizer.fit_transform(college_features)
    #     cosine_similarities = linear_kernel(college_tfidf, college_tfidf)
    #     college_indices = pd.Series([i for i in range(len(colleges))], index=[college.name for college in colleges])
    #     content_based_colleges = []
    #     for i in range(len(cosine_similarities)):
    #         similar_indices = cosine_similarities[i].argsort()[:-6:-1]
    #         content_based_colleges.append(college_indices.iloc[similar_indices].index.tolist()[1:])
       
    #     # Compute collaborative filtering recommendations
    #     reviews = Review.objects.all()
    #     df = pd.DataFrame(list(reviews.values()))
    #     reader = Reader(rating_scale=(1, 5))
    #     data = Dataset.load_from_df(df[['user_id', 'college_id', 'rating']], reader)
    #     trainset, testset = train_test_split(data, test_size=0.2)
    #     algo = SVD()
    #     algo.fit(trainset)
    #     collab_based_colleges = []
    #     for uid in df['user_id'].unique():
    #         college_predictions = []
    #         for cid in df['college_id'].unique():
    #             college_predictions.append((cid, algo.predict(uid, cid).est))
    #         college_predictions.sort(key=lambda x: x[1], reverse=True)
    #         collab_based_colleges.append([x[0] for x in college_predictions][:5])
       
    #     # Merge and filter recommendations
    #     recommended_colleges = []
    #     for i in range(len(colleges)):
    #         if location in college_features[i] and size in college_features[i] and program in college_features[i] and culture in college_features[i]:
    #             content_based = content_based_colleges[i]
    #             collab_based = collab_based_colleges[i]
    #             recommendations = list(set(content_based + collab_based))
    #             recommended_colleges.append(recommendations[:5])



    degrees = Degree.objects.all()
    context = {
        "colleges": colleges,
        "search_college": search_college,
        "degrees":degrees
    }
    return render(request, 'college/college.html', context)

@login_required(login_url = 'login')
def add_news_letter(request):
    form = NewsLetterForm(request.POST)
    if form.is_valid():
        news_letter = form.save(commit=False)
        news_letter.created_by = request.user
        news_letter.save()
    
    return JsonResponse({'status': True})

@login_required(login_url = 'login')
def college_detail(request, pk):
    college = College.objects.get(id = pk)
    degrees = CollegeDegree.objects.filter(college = pk)
    streams = CollegeStream.objects.filter(college = pk)
    questions = CollegeQuestion.objects.filter(college = pk)
    context = {
        "college": college,
        "degrees": degrees,
        "streams": streams,
        "questions": questions,
    }
    return render(request, 'college/college_detail.html', context)

@login_required(login_url = 'login')
def study_abroad(request):
    return render(request, 'college/study_abroad.html')

@login_required(login_url = 'login')
def profile(request):

    user = UserDetail.objects.filter(user = request.user).first()
    educations = Education.objects.filter(user = request.user)
    context = {
        "user": user,
        "educations": educations
    }
    return render(request, 'college/profile.html', context)

@login_required(login_url = 'login')
def filter_college(request):
    data = {}
    degree = request.POST.get("degree")
    degree = CollegeDegree.objects.filter(degree = degree)
    college_list = []
    for deg in degree:
        col = College.objects.get(id = deg.college.id)   
        college_list.append(col)

    print(college_list)
    data['html'] = render_to_string('college/college_list.html', {"colleges": college_list})
    data["success"] = True
    return JsonResponse(data)


def add_education(request):
    form = AddEducation()
    if request.method == 'POST':
        form = AddEducation(request.POST)
        print(form.is_valid())
        if form.is_valid():
            edu = form.save(commit=False)
            edu.user = request.user
            edu.created_by = request.user
            edu.save()
            return redirect('profile')
    context = {
        "form": form
    }

    return render(request, 'college/add_education.html', context)

def add_profile(request):
    user = UserDetail.objects.filter(user = request.user).first()
    
    if request.method == 'POST':
        form = AddProfile(request.POST, instance=user)
        print(request.POST)
        print(form.is_valid())
        print(form.errors)
        print(form.non_field_errors)

        if form.is_valid(): 
            print("grtf")
            user = form.save(commit=False)
            user.user = request.user
            user.created_by = request.user
            user.save()
            return redirect('profile')
        else:
            if form.non_field_errors():
                # Print non_field_errors
                for error in form.non_field_errors():
                    print(error)
    form = AddProfile(instance=user)
    context = {
        "user": user,
        "form": form,
    }
    return render(request, 'college/add_profile.html', context) 


def save_conselling(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        message = request.POST.get('message')
        data = CounsellingData.objects.create(
            name = name,
            email = email,
            number = number,
            message = message,
            created_by = request.user
        )
    return JsonResponse({'status': True, "data": model_to_dict(data)})