# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path,include
from . import views
from .views import CustomerProfileView,SellerProfileView,LoginView
from rest_framework import routers
from django.conf.urls import url

router = routers.DefaultRouter()


urlpatterns = [
 path("", views.home, name="home"),
 #path("create/",UserProfileView.as_view(),name='usercreate'),
 url(r'^user/$',views.CustomerProfileView.as_view(),name='user_list'),
 url(r'^seller/$',views.SellerProfileView.as_view(),name='seller_list'),
 url(r'^login/$',views.LoginView.as_view(),name="login"),
]