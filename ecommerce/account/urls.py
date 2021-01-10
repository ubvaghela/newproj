# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls import url


urlpatterns = [
 path("login",views.login_user,name="login"),
 path("logout",views.logout_user,name="logout"),
 path("usersignup",views.user_signup,name="user_signup"),
 path("sellersignup",views.seller_signup,name="seller_signup"),
 path("profile/",views.profile_update,name="profile_update"),
]