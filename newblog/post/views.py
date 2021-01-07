from django.shortcuts import render,get_object_or_404
from .models import Post
from django.http import Http404
from .forms import PostForm

# Create your views here.
def post(request,id):
    try:
        post = Post.objects.get(id=id)
        params={'blogpost':post}
    except Post.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request,'post/index.html',params)

def post_update(request):
    obj =get_object_or_404(Post,id=1)
    initial_data = {
        'title':obj.title,
        'content':obj.content,
    }
    form = PostForm(request.POST or None, initial=initial_data,)
    if form.is_valid():
        title = form.cleaned_data['title']
        content = form.cleaned_data['content']
        save_post = Post(id=1,author=request.user,title=title,content=content)
        save_post.save()
    context = {'form':form}
    return render(request,'post/post_update.html',context)