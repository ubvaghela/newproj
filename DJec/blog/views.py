from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog
from django.core.paginator import Paginator

# Create your views here.

def index(request):
	blogpost = Blog.objects.order_by('post_id').reverse()
	params = {'blogpost':blogpost}
	print(blogpost)
	return render(request,'blog/index.html',params)
    #return HttpResponse("Blog Index Page ")

def blogpost(request,id):
	post = Blog.objects.filter(post_id=id)[0]

	allpost = Blog.objects.reverse()
	paginator = Paginator(allpost,1)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	print(page_obj)

	params  = {'post':post,'page_obj':page_obj}
	return render(request,'blog/blogpost.html',params)