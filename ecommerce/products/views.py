# -*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from .models import Product
from category.models import Subcategory
from  home.views import category


def home(request,slug=None):
    context = category(request)
    if slug:
        get_slug = get_object_or_404(Subcategory,slug=slug)
        all_products = Product.objects.filter(subcategory=get_slug.id).all()
    else:
        all_products = Product.objects.all()
    context['all_products'] = all_products
    return render(request,'products/index.html',context)


def product_detail(request,id,slug):
    context = category(request)
    product = Product.objects.get(pk=id)
    context['product_dtls'] = product
    #context = {'product_dtls':product}
    return render(request,'products/product_detail.html',context)


def get_input_product_detail(request):
    input_detail = {
        'name' : request.POST.get('name'),
        'subcategory' : Subcategory.objects.get(id=request.POST.get('subcategory')),
        'description' : request.POST.get('description'),
        'price' : request.POST.get('price'),
        'available_qty' : request.POST.get('available_qty'),
        'buffer_qty' : request.POST.get('buffer_qty'),
        'image' : request.FILES.get('image'),
        'seller_id' : request.user,
        }
    return input_detail


def add_product(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            input_detail = get_input_product_detail(request)
            save_product = Product(
                    name = input_detail['name'],
                    subcategory = input_detail['subcategory'],
                    description = input_detail['description'],
                    price = input_detail['price'],
                    available_qty = input_detail['available_qty'],
                    buffer_qty = input_detail['buffer_qty'],
                    image = input_detail['image'],
                    seller_id = input_detail['seller_id']
                )
            save_product.save()
            messages.success(request,'Product add Successfully')
            return redirect('home')
    else:
        messages.error(request,'Login Require')
        return redirect('login')
    context = category(request)
    return render(request,"products/add_product.html",context)


def update_product(request,slug,id):
    if request.user.is_authenticated:
        product = get_object_or_404(Product,id=id)
        if request.user.id == product.seller_id.id:
            if request.method == "POST":
                input_detail = get_input_product_detail(request)
                save_product = Product(
                    id = id,
                    name = input_detail['name'],
                    subcategory = input_detail['subcategory'],
                    description = input_detail['description'],
                    price = input_detail['price'],
                    available_qty = input_detail['available_qty'],
                    buffer_qty = input_detail['buffer_qty'],
                    image = input_detail['image'],
                    seller_id = input_detail['seller_id']
                )
                save_product.save()
                messages.success(request,'Product Updated Successfully')
                return redirect(f'/{slug}/{id}')
        else:
            messages.error(request,'You are unauthorized to access this page')
            return redirect('home')
        context = category(request)
        context['product_dtls'] = product
        context['slug'] = slug
        return render(request,'products/update_product.html',context)
    else:
        return redirect('home')


def delete_product(request,id):
    if request.user.is_authenticated:
        product = get_object_or_404(Product,id=id)
        if request.user.id == product.seller_id.id:
            if request.method == "POST":
                product.delete()
                messages.success(request,"Product Delete Successfully")
                return redirect('home')
            else:
                return redirect('home')
        else:
            messages.error(request,'You are unauthorized to do this Operation')
            return redirect('home')
    else:
        return redirect('login')
    




        
