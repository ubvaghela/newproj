# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls import url


urlpatterns = [
    path('',views.home,name="home"),
    path("products/addnew", views.add_product, name="add_product"),
    path("<int:id>/delete",views.delete_product,name="delete_product"),
    path('<str:slug>',views.home,name="home"),
    path("<str:slug>/<int:id>", views.product_detail, name="product_detail"),
    path("<str:slug>/<int:id>/update_product", views.update_product, name="update_product"),
]