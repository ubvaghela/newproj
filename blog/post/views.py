from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post, PostLike, PostComment, Profile
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from .forms import SignUpForm,PostForm,PostLikeForm,ChangePasswordForm,PasswordResetEmailForm,ResetPasswordForm,ProfileForm
from post.templatetags import extras
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.core.mail import send_mail

from django.utils.http import int_to_base36, base36_to_int, urlsafe_base64_decode,urlsafe_base64_encode,base64
from django.contrib.auth.tokens import default_token_generator

# Create your views here.

def blogpost(request,id):
    try:
        blogposts = Post.objects.get(id=id)
        #createpostlike=PostLike.objects.create(post_id=id)
        #createpostlike.save()
        comments = PostComment.objects.filter(post=id,parent=None)
        replies = PostComment.objects.filter(post=id).exclude(parent=None)
        repliesDict = {}
        
        for reply in replies:
            if reply.parent.id not in repliesDict.keys():
                repliesDict[reply.parent.id]=[reply]
            else:
                repliesDict[reply.parent.id].append(reply)
        postlikes = PostLike.objects.values('likes').filter(post_id=id)
        if {'likes':request.user.id} not in postlikes:
            userexe = 'btn btn-light'
            liketf='f'
        elif request.user.id==None:
            userexe = 'btn btn-light'
            liketf='f'
        else:
            userexe='btn btn-primary'
            liketf='t'
        
        if postlikes[0]['likes']==None:
            postlikes={}
        params={'blogposts':blogposts,"comments":comments,'postlikes':len(postlikes),'userexe':userexe,'liketf':liketf,'replies':repliesDict}
        return render(request,'post/post.html',params)
    except:
        return render(request,'post/post.html',{})

@csrf_exempt
def likepost(request,id):
    
    if request.user.is_authenticated:
        if request.is_ajax():
            liketf = request.POST['liketf']
            username = request.user.id
            inslike=get_object_or_404(PostLike,post_id=id)

            if liketf=='f':
                userlike = inslike.likes.add(username)
            else:
                userlike = inslike.likes.remove(username)
        
            form = PostLikeForm(userlike or None, instance=inslike)
            if form.is_valid():
                form.save_m2m()
                return redirect(f'/post/{id}')
            return redirect(f'/post/{id}')
    #else:
    #    return redirect(f'/post/{id}')
    return redirect(f'/post/{id}')


def updatelike(request,id):
    postlikes = PostLike.objects.values('likes').filter(post_id=id)
    if request.user.is_authenticated:
        if postlikes[0]['likes']==None:
            postlikes={}
        return HttpResponse(len(postlikes))
    else:
        if postlikes[0]['likes']==None:
            postlikes={}
        return HttpResponse(len(postlikes))

def post_delete(request,id):
    try:
        blogposts = Post.objects.get(id=id) 
        if request.user.is_authenticated and request.user.username==blogposts.author.username:
            blogpost.delete()
            messages.success(request,('Post Deleted Successfully'))
            return redirect('/')
        else:
            messages.error(request,('You are Unauthorized Person'))
            return redirect('/')
    except:
        messages.error(request,('Sorry, Page Not Found'))
        return redirect('/')

def login_user(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,('You have Successfully Login'))
                return redirect('/')
            else:
                messages.error(request,('Error'))
                return redirect('login_user')   
        return render(request,'post/login.html',{})
    else:
        return redirect('/')

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,('You Have Successfully logout!'))
        return redirect('/')
    else:
        return redirect('/post/login/')

def password_change(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            item = get_object_or_404(User,username=request.user)
            form = ChangePasswordForm(request.POST,item)
            currentpassword= request.user.password
            if form.is_valid():
                if check_password(request.POST['old_password'],currentpassword):
                    item.set_password(request.POST['new_password'])
                    item.save()
                    update_session_auth_hash(request, item)
                    messages.success(request,'Password Change Successfully.')
                    return redirect('/')
                else:
                    messages.error(request, 'Old Password is Incorrect.')
        else:
            form = ChangePasswordForm()
        context={"form":form}
        return render(request,'post/password_change.html',context)
    else:
        return redirect('/post/login/')

def signup_user(request):
    #data=self.reuest.POST.get
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request,username=username,password=password)
            login(request,user)
            messages.success(request,('You have Successfully Login'))
            return redirect('/')
    else:
        form = SignUpForm()
    context={'form':form}
    return render(request,'post/signup.html',context)

def add_post(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post_item = form.save(commit=False)
                post_item.author = request.user
                #post_item.likes = request.user
                post_item.save()
                newpostlike = PostLike(post_id_id=post_item.id)
                newpostlike.save()
                return redirect('/')
        else:
            form = PostForm()
        context = {'form':form,'post_label':'Add New Post'}
        return render(request,'post/post_form.html',context)
    else:
        return redirect('/post/login/')

def edit_post(request,id):
    if request.user.is_authenticated:
        item = get_object_or_404(Post,id=id)
        if request.user.username==item.author.username:
            form = PostForm(request.POST or None, instance=item)
            if form.is_valid():
                form.save()
                return redirect('/')
            context={'form':form,'post_label':'Edit Post'}
            return render(request,'post/post_form.html',context)
        else:
            return redirect('/')
    else:
        return redirect('/post/login/')

def comments(request,id):
    if request.user.is_authenticated and request.method=="POST":
        username = request.user
        usercomment = request.POST['usercomment']
        main_comment = int(request.POST['main_comment'])
        print(main_comment)
        post = Post.objects.get(id=id)
        if main_comment==0:
            comment = PostComment(user=username,post=post,comment=usercomment)
            messages.success(request,'Comment Post Successfully')
        else:
            main_comment = PostComment.objects.get(id=main_comment)
            comment = PostComment(user=username,post=post,parent=main_comment,comment=usercomment)
            messages.success(request,'Comment Reply added Successfully')
        comment.save()
    else:
        messages.error(request,'Login Require for comment')
        return redirect('/post/login/')
    return redirect(f'/post/{id}/')

# Password Reset 
#from django.utils.encoding import force_text
def password_reset(request):
    if request.method=="POST":
        form = PasswordResetEmailForm(request.POST)
        if form.is_valid():
            user_email = User.objects.get(email=request.POST['email'])
            token_generator = default_token_generator
            
            token=token_generator.make_token(user_email)
            #d = force_text(urlsafe_base64_encode(user_email))
            uid = int_to_base36(user_email.pk)
            
            link = f"http://127.0.0.1:8000/post/password_reset_confirm/{uid}/{token}/"
            send_mail('Request Submitted',link,'infohelp@myblog.com',[request.POST['email']])
            messages.success(request,f'Password Reset Link Sent to {request.POST["email"]}')
            return redirect('/')
    else:
        form = PasswordResetEmailForm()
    context={"form":form}
    return render(request,"post/password_reset_form.html",context)

def password_reset_confirm(request,uidb36=None,token=None):
    #print(uidb36,token) password_reset_complete.html
    try:
        uid=base36_to_int(uidb36)
        user = User.objects.get(id=uid)

        token_generator = default_token_generator
        used_token_check = token_generator.check_token(user, token)
        if used_token_check==True:
            if request.method=="POST":
                form = ResetPasswordForm(request.POST,uidb36,token)
                if form.is_valid() and used_token_check==True:
                    user.set_password(request.POST['new_password'])
                    user.save()
                    messages.success(request,'Password Reset Successfully. Login with New Credentials')
                    return redirect('/post/login/')
                else:
                    messages.error(request,'Wrong Reset Password Link OR Password Link already Used')
            else:
                form = ResetPasswordForm()
            param={'form':form,'uidb36':uidb36,'token':token}
            return render(request,'post/password_reset_confirm.html',param)
        else:
            messages.error(request,'Invalid Url')
            return redirect('/')
    except:
        messages.error(request,'Invalid Url')

def password_reset_complete(request):
    return render(request,'post/password_reset_complete.html')

@login_required(login_url='/post/login/')
def user_profile(request):
    profile_data = Profile.objects.get(user=request.user) 
    return render(request,'post/profile.html',{'profile_data':profile_data})

@login_required(login_url='/post/login/')
def update_profile(request):
    item = get_object_or_404(Profile,user=request.user.id)
    if request.method == 'POST':
        form = ProfileForm(request.POST or None,request.FILES,instance=item)
        if form.is_valid():
            form.save()
            messages.success(request,'Your profile was successfully updated!')
            return redirect('/post/profile/')
    else:
        form = ProfileForm(instance=item)
        print(form)
    return render(request, 'post/update_profile.html', {'form': form})

#Dise.objects.filter(id__in = [1,6])
#if not Dise.objects.filter(id__notin = [1,6])