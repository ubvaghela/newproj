# -*- coding: utf-8 -*-
from django.shortcuts import render
import stripe
import json

stripe.api_key = 'sk_test_51I8iATIqXYelWJBByYQUj7VUiZEQN8bqB21s3Mr1wtaCrD3bkIu5zIXp08MecUfzrPORzz4FS0nj1jYoIEg0n6NZ004Gb29U5r'

def payment_index(request):
    charge = stripe.Charge.retrieve("ch_1I8g7a2eZvKYlo2C6PvuabPa",stripe_account="acct_1032D82eZvKYlo2C")
    print(charge)
    #charge.save()
    context = {'charge':charge}
    return render(request,'payment/payment.html',context)

