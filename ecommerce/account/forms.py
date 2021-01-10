# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile,User


class UserForm(forms.Form):
    first_name = forms.CharField(initial='',widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(initial='',widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(initial='',widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(initial='',widget=forms.PasswordInput(attrs={'class':'form-control'}))


class UserSignupForm(UserForm):
    address = forms.CharField(initial='',widget=forms.Textarea(attrs={'class':'form-control'}))
    #city = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),initial='')
    #state = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),initial='')
    zipcode = forms.IntegerField(initial='',widget=forms.NumberInput(attrs={'class':'form-control'}))
    mobile_number = forms.IntegerField(initial='',widget=forms.NumberInput(attrs={'class':'form-control'}))


class SellerSignupForm(UserSignupForm):
    gst_no = forms.IntegerField(initial='',widget=forms.NumberInput(attrs={'class':'form-control'}))
    bank_account_number = forms.IntegerField(initial='',widget=forms.NumberInput(attrs={'class':'form-control'}))


class UserProfileForm(UserSignupForm):
    
    def __init__(self,*args, **kwargs):
        super(UserProfileForm,self).__init__(*args, **kwargs)
        self.fields.pop('first_name',)
        self.fields.pop('last_name',)
        self.fields.pop('email',)
        self.fields.pop('password',)