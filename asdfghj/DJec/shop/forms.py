from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django import forms
from django.contrib.auth.models import User

class EditprofileForm(UserChangeForm):
	"""docstring for EditprofileForm"""
	password = forms.CharField(label="",widget=forms.TextInput(attrs={'type':'hidden','class':'form-control'}))
	class Meta:
		model = User
		fields=('username','first_name','last_name','email','password')

	def __init__(self, *args, **kwargs):
	    super(EditprofileForm, self).__init__(*args, **kwargs)

	    self.fields['username'].widget.attrs['class']= 'form-control'
	    self.fields['first_name'].widget.attrs['class']= 'form-control'
	    self.fields['last_name'].widget.attrs['class']= 'form-control'
	    self.fields['email'].widget.attrs['class']= 'form-control'



class SignUpForm(UserCreationForm):
	
	email = forms.EmailField(label="Enter Your Email Address",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Email Address'}))
	first_name = forms.CharField(label="First Name",max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your First Name'}))
	last_name = forms.CharField(label="Last Name",max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your Last Name'}))

	class Meta:
		model = User
		fields = ('username','first_name','last_name','email','password1','password2')

	def __init__(self,*args,**kwargs):
		super(SignUpForm,self).__init__(*args,**kwargs)

		self.fields['username'].widget.attrs['class']= 'form-control'
		self.fields['username'].widget.attrs['placeholder']= 'Your UserName'
		self.fields['username'].label="UserName"
		self.fields['username'].help_text='<small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small>'


		self.fields['password1'].widget.attrs['class']= 'form-control'
		self.fields['password1'].widget.attrs['placeholder']= 'Enter Your Password'
		self.fields['password1'].label='Password'

		self.fields['password2'].widget.attrs['class']= 'form-control'
		self.fields['password2'].widget.attrs['placeholder']= 'Confirm Your Password'
		self.fields['password2'].label='Confirm Password'

class ChangePassword(PasswordChangeForm):
	def __init__(self, user, *args, **kwargs):
		super(ChangePassword, self).__init__(user,*args, **kwargs)
		self.fields['old_password'].widget.attrs.update({'class': 'form-control'})
		self.fields['new_password1'].widget.attrs.update({'class': 'form-control'})
		self.fields['new_password2'].widget.attrs.update({'class': 'form-control'})