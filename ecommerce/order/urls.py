# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls import url


urlpatterns = [
    path('checkout',views.checkout,name="checkout"),
    #path('create-checkout-session',views.create_checkout_session,name="create_checkout_session"),
    path('charge',views.charge,name="charge")
]