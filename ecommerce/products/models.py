# -*- coding: utf-8 -*-
from django.db import models
from category.models import Subcategory
from account.models import User


class Product(models.Model):
    name = models.CharField(max_length=100)
    subcategory = models.ForeignKey(Subcategory,on_delete=models.CASCADE)
    description = models.TextField()
    price = models.PositiveIntegerField(blank=True,null=True)
    available_qty = models.PositiveIntegerField(blank=True,null=True)
    buffer_qty = models.PositiveIntegerField(blank=True,null=True)
    image = models.ImageField(upload_to='product_image')
    seller_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    