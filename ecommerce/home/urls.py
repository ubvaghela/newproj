# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls import url


urlpatterns = [
 path("about", views.about, name="about"),
 path("contact", views.contact, name="contact"),
 path("",views.category,name="category"),
]