# -*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Checkout,Order,OrderItem,Product
import json
import stripe
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.core.mail import send_mail


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
        
        #Payment Method is Case on Delivery
        if payment_method=="COD":
            place_order = order_object_save(request,str_to_json,checkout)
            context = {"order_id":place_order}
            temp = 'order/success.html'
            temp_ret(temp)
        else:
            payment_status = 'DONE'
            stripeToken = request.POST.get('stripeToken')
            # Create account in stripe 
            account = stripe.Account.create(
                country = "IN",
                type="custom",
                email=request.user,
                capabilities={
                    'card_payments':{
                        'requested':True,
                    },
                    'transfers':{
                        'requested':True,
                    },
                },
            )
            # Create customer in stripe 
            customer = stripe.Customer.create(
                address = {
                    'line1':address,
                    'city':city,
                    'state':state,
                    'postal_code':zipcode,

                },
                email=request.user,
            )
            # Create charges for customer in stripe 
            charge = stripe.Charge.create(
                source=stripeToken,
                amount = amount,
                currency = "inr", 
            )
            context = {"order_id":"place_order"}
            place_order = order_object_save(request,str_to_json,checkout)
            send_order_success_email(request,place_order,str_to_json)
            context = {"order_id":place_order}
            temp = 'order/success.html'
            temp_ret(temp)
    return render(request,temp_ret(f'{temp}'),context)


#   Return order Success Template
def temp_ret(temp):
    return temp


#   Save Order and OrderItem Objects
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


# send mail in console
def send_order_success_email(request,place_order,str_to_json):
    order_details = f'Thank you for Order \n Your order id :{place_order} \n order Items :  {str_to_json}'
    customer_email = request.user
    send_mail('SALE Order',order_details,'customer@sale.com',[customer_email],fail_silently=False,)
    