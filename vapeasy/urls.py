from django.contrib import admin
from django.urls import path, include
from .import views

app_name = 'vapeasy'

urlpatterns = [
    path('', views.index, name='index'),
    path('survey/', views.survey, name='survey'),
    path('review_list/', views.review_list, name='review_list'),
    path('review_detail/<int:review_id>/', views.review_datail, name='review_detail'),
    path('review/create/', views.review_create, name='review_create'),
]
