from django.urls import path
from college import views

urlpatterns = [
    path('', views.home, name='home'),
    path('college', views.college, name='college'),
    path('college/<int:pk>', views.college_detail, name='college.detail'),
    path('news-letter/create', views.add_news_letter, name='newsletter.create'),
    path('study-abroad', views.study_abroad, name='study-abroad'),
]