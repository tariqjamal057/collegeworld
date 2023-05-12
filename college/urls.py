from django.urls import path
from college import views

urlpatterns = [
    path('', views.home, name='home'),
    path('college', views.college, name='college'),
    path('news-letter/create', views.add_news_letter, name='newsletter.create'),
]