from django.shortcuts import render
from .models import Post
from django.http import Http404

# Create your views here.
def post(request,id):
    try:
        post = Post.objects.get(id=id)
        params={'blogpost':post}
    except Post.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request,'post/index.html',params)