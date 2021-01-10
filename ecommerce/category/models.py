# -*- coding: utf-8 -*-
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Subcategory(models.Model):
    category_name = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="subcategory")
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    