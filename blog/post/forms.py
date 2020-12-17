from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
from django.forms import ModelForm
from .models import Post, PostLike,Profile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Enter Your Email Address", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Email Address'})) 
    first_name = forms.CharField(label="First Name",max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Firstname'})) 
    last_name = forms.CharField(label="Last Name",max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Lastname'})) 

    class Meta:
        model = User
        fields = ('first_name','last_name','email','username','password1','password2')
    
    def __init__(self,*args,**kwargs):
        super(SignUpForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']= 'form-control'
        self.fields['password2'].widget.attrs['class']= 'form-control'

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'birth_date' , 'photo']
        widgets = {'birth_date': forms.DateInput(format=('%m-%d-%Y'), attrs={'class':'form-control w-25 px-2', 'placeholder':'Select a date', 'type':'date'}),}
    
    def __init__(self,*args,**kwargs):
        super(ProfileForm,self).__init__(*args,**kwargs)
        self.fields['bio'].widget.attrs['class']='form-control'
        self.fields['bio'].label="Biodata"
        self.fields['location'].widget.attrs['class']='form-control'
        self.fields['photo'].widget.attrs['class']='form-control'


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title','slug','content']
    
    def __init__(self,*args,**kwargs):
        super(PostForm,self).__init__(*args,**kwargs)
        self.fields['title'].widget.attrs['class']='form-control'
        self.fields['title'].label="Title"
        self.fields['title'].help_text='<small>Required.</small>'
        self.fields['slug'].widget.attrs['class']='form-control'
        self.fields['slug'].label="Slug"
        self.fields['slug'].help_text='<small>Required. Example : hello-world </small>'
        self.fields['content'].label='Details'
        #self.fields['author'].widget.attrs['type']= 'hidden'

class PostLikeForm(ModelForm):
    class Meta:
        model = PostLike
        fields = ['likes']

class ChangePasswordForm(forms.Form):
    
    old_password=forms.CharField(label="Old Password",max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Old Password'}))
    new_password=forms.CharField(label="New Password",max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter New Password'}))

class PasswordResetEmailForm(forms.Form):
    email = forms.EmailField(label="Enter Your Email Address", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Email Address'}))

class ResetPasswordForm(forms.Form):
    new_password=forms.CharField(label="New Password",max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter New Password'}))
    conf_new_password=forms.CharField(label="Confirm Password",max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter New Password'}))

    def clean(self):
        cleaned_data = super(ResetPasswordForm,self).clean()
        new_password = cleaned_data.get('new_password')
        conf_new_password = cleaned_data.get('conf_new_password')

        if new_password!=conf_new_password:
            raise forms.ValidationError("password and confirm_password does not match")

