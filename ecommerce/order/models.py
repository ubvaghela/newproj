# -*- coding: utf-8 -*-
from django.db import models
from account.models import User
from products.models import Product


PAYMENT_STATUS_CHOICES = [
    ('PENDING','Pending'),
    ('DONE','Done'),
]


PAYMENT_METHOD_CHOICES = [
    ('COD','Cash on Delivery'),
    ('CREDIT','credit'),
    ('DEBIT','debit'),
]


ORDER_STATUS = [
    ('PENDING','Pending'),
    ('ONWAY','On the Way'),
    ('DONE','Done'),
]


class Checkout(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()
    payment_status = models.CharField(choices=PAYMENT_STATUS_CHOICES, max_length=50,default="PENDING")
    payment_method = models.CharField(choices=PAYMENT_METHOD_CHOICES, max_length=50)

    def __str__(self):
        return str(self.id)


class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    checkout = models.ForeignKey(Checkout,on_delete=models.CASCADE,verbose_name = u'Checkout Details')
    order_status = models.CharField(choices=ORDER_STATUS, max_length=50,default="PENDING")
    
    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    order_qty = models.PositiveIntegerField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.order_id.user.email


    
