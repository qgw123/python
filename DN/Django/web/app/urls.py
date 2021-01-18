__author__ = '秋轩'
from django.contrib import admin
from django.urls import path,re_path,include
from app import views
urlpatterns = [
    re_path('^$',views.index, name='index'),
    re_path('(?P<question_id>\d+)/$',views.detail, name='detail'),
    re_path('(?P<question_id>\d+)/result/$',views.result,name='result'),
    re_path('(?P<question_id>\d+)/vote/$',views.vote,name='vote'),

    # path('register/',views.register),
]

