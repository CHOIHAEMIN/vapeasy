from django.contrib import admin
from django.urls import path, include
from .views import base_views, review_views, comment_views, vote_views

app_name = 'vapeasy'

urlpatterns = [
    # base_views.py
    path('', base_views.index, name='index'),
    path('survey/', base_views.survey, name='survey'),
    
    # review_views.py
    path('review_list/', review_views.review_list, name='review_list'),
    path('review_detail/<int:review_id>/', review_views.review_datail, name='review_detail'),
    path('review/create/', review_views.review_create, name='review_create'),
    path('review/modify/<int:review_id>/', review_views.review_modify, name='review_modify'),
    path('review/delete/<int:review_id>/', review_views.review_delete, name='review_delete'),
    
    # comment_views.py
    path('comment/create/review/<int:review_id>/', comment_views.comment_create_review, name='comment_create_review'),
    path('comment/modify/review/<int:comment_id>/', comment_views.comment_modify_review, name='comment_modify_review'),
    path('comment/delete/review/<int:comment_id>/', comment_views.comment_delete_review, name='comment_delete_review'),
    
    # vote_views.py
    path('vote/review/<int:review_id>/', vote_views.vote_review, name='vote_review'),
    path('vote/comment/<int:comment_id>/', vote_views.vote_comment, name='vote_comment'),

]
