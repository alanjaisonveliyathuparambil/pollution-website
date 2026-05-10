from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('air/', views.air, name='air'),
    path('water/', views.water, name='water'),
    path('noise/', views.noise, name='noise'),
    path('soil/', views.soil, name='soil'),
    path('quiz-intro/', views.quiz_intro, name='quiz_intro'),
    path('quiz/', views.quiz, name='quiz'),
]