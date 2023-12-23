from django.shortcuts import render
from django.urls import path,include
from . import views

# Create your views here.

urlpatterns = [
    path('<int:pk>/', views.single_post_page),
    path('', views.notice),
    path('create_post/', views.PostCreate.as_view()),

]
