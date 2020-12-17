from django.forms import ModelForm
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email','subject']

    def __init__(self,*args,**kwargs):
        super(ContactForm,self).__init__(*args,**kwargs)
        self.fields['name'].widget.attrs['class']='form-control'
        self.fields['name'].label="Name"
        self.fields['email'].widget.attrs['class']='form-control'
        self.fields['email'].label="Email"
        self.fields['subject'].widget.attrs['class']='form-control'
        self.fields['subject'].label='Subject'