from django.shortcuts import render
from post.models import Post
from django.http import HttpResponse,JsonResponse
from django.core import serializers
import json

# Create your views here.

def index(request, user=None):
    #posts = Post.objects.all()
    #params = {'posts':posts}
    return render(request,'home/index.html',{})

def about(request):
    return render(request,'home/about.html',{})

def contact(request):
    return render(request,'home/contact.html',{})

def search(request):
    if request.GET.get('query'):
        query = request.GET.get("query")
        query = Post.objects.all().filter(title__icontains=query)
        context = serializers.serialize('json',query)
        output = [item for item in json.loads(context)]
        return JsonResponse({"data":output})
    else:
        query = Post.objects.all()
        context = serializers.serialize('json',query)
        output = [item for item in json.loads(context)]
        return JsonResponse({"data":output})