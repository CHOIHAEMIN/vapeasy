from cgitb import handler
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import accounts.views
from .views import base_views, review_views, comment_views, vote_views, survey_views, product_views

app_name = 'vapeasy'

urlpatterns =  [
    # base_views.py
    path('', base_views.index, name='index'),
    
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
    
    # survey_views.py
    path('survey/', survey_views.survey, name='survey'),
    path('survey/answer/', survey_views.survey_answer, name='survey_answer'),
    path('result/', survey_views.survey_result, name='survey_result'),

    # product_views.py
    path('product_list/', product_views.product_list, name='product_list'),

    # oauth/views.py
    path('oauth/', accounts.views.oauth, name='oauth'),
    path('kakao_login/', accounts.views.kakao_login, name='kakao_login'),


] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
#                                       실제 파일의 위치
# 실제 사용자에게 제공하기 위해 업로드된 파일의 url필요
