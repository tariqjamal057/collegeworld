from django.urls import path
from college import views

urlpatterns = [
    path('', views.home, name='home'),
    path('college', views.college, name='college'),
    path('college/<int:pk>', views.college_detail, name='college.detail'),
    path('college/filter', views.filter_college, name='college.filter'),
    path('news-letter/create', views.add_news_letter, name='newsletter.create'),
    path('study-abroad', views.study_abroad, name='study-abroad'),
    path('profile', views.profile, name='profile'),
    path('profile/add-edu', views.add_education, name='profile.add-edu'),
    path('profile/create', views.add_profile, name='profile.create'),
    path('counselling/create', views.save_conselling, name='counselling.create'),
]