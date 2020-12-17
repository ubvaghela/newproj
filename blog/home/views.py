from django.shortcuts import render, redirect
from post.models import Post
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import ContactForm
from django.core.mail import send_mail
from blog import settings

# Create your views here.

def index(request,user=None):
	try:
		if request.GET['user'] != None:
			posts = Post.objects.filter(author=request.user.id)
			page_obj=postPaginator(request.GET.get('page'),posts)
		params = {'posts':page_obj}
	except:
		posts = Post.objects.all()
		page_obj=postPaginator(request.GET.get('page'),posts)
		params = {'posts':page_obj}
	return render(request,'home/index.html',params)

def search(request):
	search_text = request.GET.get('srctxt')
	search_text = "" if search_text==None else search_text
	posts = Post.objects.filter(Q(title__icontains=search_text) | Q(content__icontains=search_text))
	page_obj=postPaginator(request.GET.get('page'),posts)
	params = {'posts':page_obj}
	return render(request,'home/index.html',params)

def postPaginator(page_number,obj):
	paginator = Paginator(obj, 2)
	page_obj = paginator.get_page(page_number)
	return page_obj


def about(request):
	return render(request,'home/about.html')

def contact(request):
	if request.method=="POST":
		form = ContactForm(request.POST)
		print(request.POST['email'])
		if form.is_valid():
			form.save()
			send_mail('Request Submitted',request.POST['subject'],'infohelp@myblog.com',[request.POST['email']])
			messages.success(request,'Your Message send Successfully')
			return redirect('/home/contact/')
	else:
		form = ContactForm()
	context={'form':form}
	return render(request,'home/contact.html',context)