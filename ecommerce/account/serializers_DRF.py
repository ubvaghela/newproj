# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import CustomerProfile,SellerProfile,User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name','last_name','email','password')
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class CustomerProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
       
    class Meta:
        model = CustomerProfile
        fields = ('user','address','city','state','zipcode','mobile_number',)

    def create(self,validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(),validated_data=user_data)
        profile, created = CustomerProfile.objects.update_or_create(user=user,**validated_data)
        return profile
        

class SellerProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
       
    class Meta:
        model = SellerProfile
        fields = ('user','business_address','city','state','zipcode','mobile_number','gst_no','bank_account_number')

    def create(self,validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(),validated_data=user_data)
        profile, created = SellerProfile.objects.update_or_create(user=user,**validated_data)
        return profile

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(required=True,write_only=True,error_messages={'required': 'Please Enter Your Password.'})