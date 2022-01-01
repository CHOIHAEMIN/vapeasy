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
    path('review/modify/<int:review_id>/', views.review_modify, name='review_modify'),
    path('review/delete/<int:review_id>/', views.review_delete, name='review_delete'),
    path('comment/create/review/<int:review_id>/', views.comment_create_review, name='comment_create_review'),
    path('comment/modify/review/<int:comment_id>/', views.comment_modify_review, name='comment_modify_review'),
    path('comment/delete/review/<int:comment_id>/', views.comment_delete_review, name='comment_delete_review'),
]
