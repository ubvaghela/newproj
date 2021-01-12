# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Checkout,Order,OrderItem

admin.site.register(Checkout)
admin.site.register(Order)
admin.site.register(OrderItem)

