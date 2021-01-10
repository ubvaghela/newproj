# -*- coding: utf-8 -*-
from django.shortcuts import render
from .serializers import UserSerializer,CustomerProfileSerializer,SellerProfileSerializer,LoginSerializer
from rest_framework import status
from rest_framework.views import APIView 
from rest_framework.permissions import AllowAny,IsAuthenticated
from base.response import getPositiveResponse,getNagativeResponse 
from rest_framework.response import Response
from .models import User,CustomerProfile,SellerProfile
from rest_framework.authentication import authenticate
from django.core import serializers
from django.views import View
import json
from django.http import JsonResponse


def home(request):
    return render(request,'index.html',{})


class CustomerProfileView(View):
    def get(self, request):
        profiles = CustomerProfile.objects.all()
        serialize_data = serializers.serialize(profiles)
        json_data = [item for item in json.loads(serialize_data)]
        return JsonResponse(json_data)
'''
class CustomerProfileView(APIView):
    permission_classes = (AllowAny,)
    
    def get(self,request):
        profiles = CustomerProfile.objects.all()
        serializer = CustomerProfileSerializer(profiles,many=True)
        response = getPositiveResponse("Customer List",status.HTTP_200_OK,serializer.data)
        return Response(response,status=response['status_code'])

    def post(self, request):
        userprofile_serializer = CustomerProfileSerializer(data=request.data)
        if userprofile_serializer.is_valid(raise_exception=ValueError):
            userprofile_serializer.create(validated_data=request.data)
            response = getPositiveResponse('Account Created Successfully',status.HTTP_201_CREATED,userprofile_serializer.data)
            return Response(response,status=response['status_code'])
        else:
            response = getNagativeResponse('Error In User Createtion',status.HTTP_400_BAD_REQUEST,userprofile_serializer.errors)
            return Response(response,status=response['status_code'])

        
class SellerProfileView(APIView):
    permission_classes = (AllowAny,)
    
    def get(self,request):
        profiles = SellerProfile.objects.all()
        serializer = SellerProfileSerializer(profiles,many=True)
        response = getPositiveResponse("Seller List",status.HTTP_200_OK,serializer.data)
        return Response(response,status=response['status_code'])

    def post(self, request):
        userprofile_serializer = SellerProfileSerializer(data=request.data)
        if userprofile_serializer.is_valid(raise_exception=ValueError):
            userprofile_serializer.create(validated_data=request.data)
            response = getPositiveResponse('Account Created Successfully',status.HTTP_201_CREATED,userprofile_serializer.data)
            return Response(response,status=response['status_code'])
        else:
            response = getNagativeResponse('Error In User Createtion',status.HTTP_400_BAD_REQUEST,userprofile_serializer.errors)
            return Response(response,status=response['status_code'])


class LoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self,request):
        user_serializer = LoginSerializer(data=request.data)
        email = request.data.get('email',None)
        password = request.data.get('password',None)
        if user_serializer.is_valid(raise_exception=ValueError):
            user = authenticate(email = email,password = password)
            if user is not None:
                response = getPositiveResponse('User Login Successfully',status.HTTP_200_OK,user_serializer.data)
            else:
                response = getNagativeResponse('Wrong email or password ',status.HTTP_400_BAD_REQUEST,user_serializer.errors)
            return Response(response,status=response['status_code'])
'''