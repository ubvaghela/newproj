# -*- coding: utf-8 -*-
from django.shortcuts import render
from category.models import Category,Subcategory
from products.models import Product


def category(request):
    query = Subcategory.objects.all().values('id','name','slug')
    context = {'data':query}
    return context

    
def about(request):
    context = category(request)
    return render(request,'home/about.html',context)


def contact(request):
    context = category(request)
    return render(request,'home/contact.html',context)

