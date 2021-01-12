# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls import url


urlpatterns = [
    path('',views.payment_index,name="payment_index"),
    #path('create-checkout-session',views.create_checkout_session,name="create_checkout_session"),
]