from django import forms
from .models import Post

class PostForm(forms.Form):
    title = forms.CharField(initial="title ")
    content = forms.CharField(initial="content ")

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.content = validated_data.get('content',instance.content)
        instance.save()
        return instance
    
    def __init__(self,*args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)