from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import Product, Contact, Order, OrderUpdate
from math import ceil
import json
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,PasswordChangeForm
from django.contrib import messages
from .forms import SignUpForm,EditprofileForm

# Create your views here.
with open('shopjson.json') as shop_json_data:
    shopdata = json.load(shop_json_data)['shopdata']

def index(request):
    allprods = Product.objects.exclude(qty=0)
    params = {'allProds':allprods, 'shopdata':shopdata}
    return render(request,'shop/index.html',params)

def search(request):
    pass


def about(request):
    return render(request,'shop/about.html')

def contact(request):
    pass

def tracker(request):
    pass

def productview(request,myid):
    myproducts_list = Product.objects.filter(id=myid)
    print(myproducts_list)
    myproducts= {"myproducts":myproducts_list}
    return render(request,'shop/productview.html',myproducts)

def checkout(request):
    if request.user.is_active:
        if request.method=='POST':
            items = request.POST.get('itemsJson')
            amount = request.POST.get('amount')
            name = request.POST.get('csname')
            email = request.POST.get('email')
            address1 = request.POST.get('address1')
            address2 = request.POST.get('address2')
            ph_no = request.POST.get('phno')
            city = request.POST.get('city')
            state = request.POST.get('state')
            zipcode=request.POST.get('zipcode')
            address = str(address1+' ')+str(address2)
            order = Order(items_json=items,amount=amount,name=name,email=email,address=address,phone=ph_no,city=city,state=state,zip_code=zipcode)
            order.save()
            update = OrderUpdate(order_id=order.order_id, update_desc="The Order Has Been Placed")
            update.save()
            strtodict = json.loads(items) 
            print(strtodict)
            msg = f'Order No :{order.order_id}\n Items Name :{strtodict.values()} '
            res = send_mail(
                subject = f'Order Confirmation - Your Order with Cozastore.com [ODNO_{order.order_id}] has been successfully placed!',
                message = f'{msg}.',
                from_email = 'ullashvaghela@gmail.com',
                recipient_list = [email],
                fail_silently=False,
            )
            thanks = True
            ids=order.order_id
            return render(request,'shop/checkout.html',{'thanks':thanks, 'id':ids})
            
        return render(request,'shop/checkout.html')
    else:
        return redirect('login')

''' User Authentication '''

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,('You Have Successfully login!'))
            return redirect('ShopHome')

        else:
            messages.success(request,('Error'))
            return redirect('login')
    return render(request,'shop/login.html',{})

def logout_user(request):
    logout(request)
    messages.success(request,('You Have Successfully logout!'))
    return redirect('ShopHome')

def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request,username=username,password=password)
            login(request,user)
            messages.success(request,('You Have Successfully Registered!'))
            return redirect('ShopHome')
    else:
        form = SignUpForm()
    context = {'form':form}
    return render(request,'shop/register.html',context)

def edit_profile(request):
    if request.method == "POST":
        form = EditprofileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,('You Have Successfully Edited Your Profile!'))
            return redirect('ShopHome')
    else:
        form = EditprofileForm(instance=request.user)
    context = {'form':form}
    return render(request,'shop/edit_profile.html',context)

def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            messages.success(request,('Your Password Change Successfully!'))
            return redirect('ShopHome')
    else:
        form = PasswordChangeForm(user=request.user)
    context = {'form':form}
    return render(request,'shop/change_password.html',context)