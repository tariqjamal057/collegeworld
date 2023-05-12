from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from college.forms import NewsLetterForm
from django.http import JsonResponse
from college.models import College


# Create your views here.
@login_required(login_url = 'login')
def home(request):
    context = {
        "newsletter": NewsLetterForm()
    }
    return render(request, 'college/home.html', context)

def college(request):
    colleges = College.objects.all()
    context = {
        "colleges": colleges
    }
    return render(request, 'college/college.html', context)

def add_news_letter(request):
    form = NewsLetterForm(request.POST)
    if form.is_valid():
        news_letter = form.save(commit=False)
        news_letter.created_by = request.user
        # news_letter.save()
    
    return JsonResponse({'status': True})