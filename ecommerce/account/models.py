# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from .user_manager import UserManager
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    username = None
    email =  models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    objects = UserManager()

    def __str__(self):
        return self.email
    

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    address = models.TextField(blank=True,null=True)
    city =  models.CharField(max_length=30,blank=True,null=True)
    state =  models.CharField(max_length=30,blank=True,null=True)
    zipcode = models.PositiveIntegerField(blank=True,null=True)
    mobile_number = models.PositiveIntegerField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email


class SellerProfile(UserProfile):
    gst_no = models.BigIntegerField(blank=False,null=False)
    bank_account_number = models.BigIntegerField(blank=False,null=False)

    def __str__(self):
        return self.user.email


class State(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class City(models.Model):
    state_id = models.ForeignKey(State,on_delete=models.CASCADE,related_name='state')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    