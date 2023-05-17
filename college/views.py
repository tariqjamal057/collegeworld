from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from college.forms import NewsLetterForm
from django.http import JsonResponse
from college.models import College, CollegeStream, CollegeDegree, CollegeQuestion
from django.core.paginator import Paginator
from django.db.models import Q


# Create your views here.
@login_required(login_url = 'login')
def home(request):
    context = {
        "newsletter": NewsLetterForm()
    }
    return render(request, 'college/home.html', context)

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
    context = {
        "colleges": colleges,
        "search_college": search_college,
    }
    return render(request, 'college/college.html', context)

def add_news_letter(request):
    form = NewsLetterForm(request.POST)
    if form.is_valid():
        news_letter = form.save(commit=False)
        news_letter.created_by = request.user
        news_letter.save()
    
    return JsonResponse({'status': True})


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


def study_abroad(request):
    return render(request, 'college/study_abroad.html')