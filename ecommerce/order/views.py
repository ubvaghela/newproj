# -*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Checkout,Order,OrderItem,Product
import json
import stripe
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect


stripe.api_key = 'sk_test_51I8iATIqXYelWJBByYQUj7VUiZEQN8bqB21s3Mr1wtaCrD3bkIu5zIXp08MecUfzrPORzz4FS0nj1jYoIEg0n6NZ004Gb29U5r'


@login_required(login_url='login')
def checkout(request):
    temp = 'order/checkout.html'
    context = {} 
    if request.method == "POST":
        user = request.user
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')
        cart_items = request.POST.get('cart_items')
        amount = request.POST.get('total')
        payment_method = request.POST.get('paymentMethod')

        str_to_json = json.loads(cart_items)
        
        checkout = Checkout(
            user=user,
            address=address,
            city=city,
            state=state,
            zipcode=zipcode,
            amount=amount,
            payment_method=payment_method
        )
        checkout.save()

        if payment_method=="COD":
            place_order = order_object_save(request,str_to_json,checkout)
            context = {"order_id":place_order}
            temp = 'order/success.html'
            temp_ret(temp)
        else:
            token = request.POST.get('stripeToken')
            print(token)
                # charge = stripe.Charge.create(
                #     amount=100,
                #     currency='inr',
                #     description='Example Charge',
                #     source = token,
                #     customer=token,
                # )
                # return render(request,'order/success.html',context)
            
                
    context = {'order':'T-Shirt'}
    return render(request,temp_ret(f'{temp}'),context)

def charge(request):
    if request.method == "POST":
        print(request.POST)
    return redirect('home')
'''
#
#   Return order Success Template
#  
'''
def temp_ret(temp):
    return temp


'''
#
#   Save Order and OrderItem Objects
#
'''
def order_object_save(request,str_to_json,checkout):
    user = request.user
    checkout = checkout
    order_status = 'PENDING'
    order = Order(
        user=user,
        checkout=checkout,
        order_status=order_status
    )
    order.save()
    for item in str_to_json:
        product = get_object_or_404(Product,id=item['product_id'])
        order_items = OrderItem(
            order_id=order,
            product_id=product,
            order_qty=item['quantity'],
            price=item['price']
        )
        order_items.save()
    return order


def create_checkout_session(request):
   pass

'''
@csrf_protect
def create_checkout_session(request):
    try:
        session = stripe.checkout.Session.create(
            payment_method_types = ['card'],
            line_items=[{
                'price_data':{
                    'currency':'usd',
                    'product_data':{
                        'name':'T-shirt',
                    },
                    'unit_amount':request.POST.get('total'),
                },
                'quantity':1,
            }],
            mode = 'payment',
            success_url = 'http://127.0.0.1:8000/order/checkout',
            cancel_url = 'http://127.0.0.1:8000/'
        )
        print(session)
        #return HttpResponse(status=200)
        return redirect('home')
    except:
         return HttpResponse(status=400)
'''