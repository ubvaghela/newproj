# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Checkout,Order,OrderItem


class CheckoutAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'state','payment_status','amount')
    list_filter = ('city','state','payment_status')
admin.site.register(Checkout, CheckoutAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'checkout', 'order_status')
    list_filter = ('user','order_status')
admin.site.register(Order, OrderAdmin)


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'product_id','order_qty','price')
    list_filter = ('product_id',)
admin.site.register(OrderItem,OrderItemAdmin)