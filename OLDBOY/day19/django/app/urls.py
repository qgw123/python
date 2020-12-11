"""Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,re_path, include
from app import views

urlpatterns = [
    path('login/', views.login),
    path('index/', views.index),
    path('user_info/', views.user_info),
    re_path('userdetail-(?P<nid>\d+)', views.userdetail),
    re_path('userdel-(?P<nid>\d+)', views.userdel),
    re_path('useredit-(?P<nid>\d+)', views.useredit),
    path('user_group/', views.group_info),
    re_path('groupdetail-(?P<nid>\d+)', views.groupdetail),
    re_path('groupdel-(?P<nid>\d+)', views.groupdel),
    re_path('groupedit-(?P<nid>\d+)', views.groupedit),
    path('orm/', views.orm),
]
