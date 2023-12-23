from django.shortcuts import render
from django.urls import path
from . import views

# Create your views here.

urlpatterns = [
    path('collabo', views.collabo),
    path('operate', views.operate),
    path('sns/', views.sns),
    path('welfare', views.welfare),
    path('intro_sns', views.intro_sns),
    path('report_sns', views.report_sns),
    path('intro_col', views.intro_col),
    path('call', views.call),
    path('intro_wel', views.intro_wel),
    path('manage', views.manage)
]
