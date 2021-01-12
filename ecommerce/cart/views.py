# -*- coding: utf-8 -*-
from django.shortcuts import render
from home.views import category


def cart_index(request):
    context = category(request)
    return render(request,'cart/index.html',context)