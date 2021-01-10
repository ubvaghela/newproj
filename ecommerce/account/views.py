# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from .models import UserProfile,SellerProfile,User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .forms import UserSignupForm,SellerSignupForm,UserProfileForm


def get_exists_user(email):
    try:
        exist_user = User.objects.filter(email=email).exists()
    except:
        return None
    return exist_user


def get_signupform_data(request):
    data =  {
        "first_name" : request.POST.get('first_name'),
        "last_name" :  request.POST.get('last_name'),
        "email" : request.POST.get('email'),
        "password" : make_password(request.POST.get('password')),
        "address" : request.POST.get('address'),
        "zipcode" : request.POST.get('zipcode'),
        "mobile_number" : request.POST.get('mobile_number'),
    }
    return data


def singnup(request):
    pass


def user_signup(request):
    if request.method =="POST":
        form = UserSignupForm(request.POST)
        data = get_signupform_data(request)
        if get_exists_user(data['email']):
           messages.error(request,"User with this Email Id already Exists") 
        else:
            if form.is_valid():
                user = User(first_name=data['first_name'],last_name=data['last_name'],email=data['email'],password=data['password'])
                user.save()
                profile = UserProfile(user_id=user.id,address=data['address'],zipcode=data['zipcode'],mobile_number=data['mobile_number'])
                profile.save()
                return redirect('home')
    else:
        form = UserSignupForm()
    context = {'form':form}
    return render(request,"account/user_signup.html",context)


def seller_signup(request):
    if request.method == "POST":
        form = SellerSignupForm(request.POST)
        data = get_signupform_data(request)
        gst_no = request.POST.get('gst_no')
        bank_account_number = request.POST.get('bank_account_number')
        if get_exists_user(data['email']):
            messages.error(request,"User with this Email Id already Exists") 
        else:
            if form.is_valid():
                user = User(first_name=data['first_name'],last_name=data['last_name'],email=data['email'],password=data['password'])
                user.save()
                profile = SellerProfile(user_id=user.id,address=data['address'],zipcode=data['zipcode'],mobile_number=data['mobile_number'],gst_no=gst_no,bank_account_number=bank_account_number)
                profile.save()
                return redirect('home')
    else:
        form = SellerSignupForm()   
    context = {'form':form}
    return render(request,'account/seller_signup.html',context)


def profile_update(request):
    get_user = get_object_or_404(UserProfile,user=request.user.id)
    initial_data = {
        'address':get_user.address,
        'zipcode':get_user.zipcode,
        'mobile_number':get_user.mobile_number
    }
    print(get_user.id)
    form = UserProfileForm(request.POST or None,initial=initial_data)   
    if form.is_valid():
        address = form.cleaned_data['address']
        zipcode = form.cleaned_data['zipcode']
        mobile_number = form.cleaned_data['mobile_number']
        save_data = UserProfile(id=get_user.id,user_id=request.user.id,address=address,zipcode=zipcode,mobile_number=mobile_number)
        save_data.save()    
        return redirect('home')
    context = {'form':form}
    return render(request,'account/profile.html',context)


def login_user(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            email = request.POST["email"]
            password = request.POST["password"]
            user = authenticate(request,email = email,password = password)
            if user is None:
                messages.error(request, "Wrong login Credential")
            else:
                login(request,user)
                messages.success(request, "Login Successfull")
                return redirect('home')
        return render(request,"account/login.html",{})
    else:
        messages.warning(request, "You are already login")
        return redirect('home')


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,('You Have Successfully logout!'))
        return redirect('home')
    else:
        return redirect('login')