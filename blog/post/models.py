from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=False)
    photo = models.ImageField(upload_to='profile/')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

#@receiver(post_save, sender=User)
#def save_user_profile(sender, instance, **kwargs):
#    instance.profile.save()
    
class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    #content = models.TextField()
    content = RichTextUploadingField(blank=True,null=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,default='ullash')
    timestamp = models.DateTimeField(default=datetime.now)
    views = models.IntegerField(default=0)
    
    #def __str__(self):
    #    return "post : "+ str(self.timestamp)
    class Meta:
        ordering = ['-id']
    

class PostLike(models.Model):
    post_id = models.ForeignKey('Post',on_delete=models.CASCADE)
    likes = models.ManyToManyField(User,blank=True)

    #def __str__(self):
    #    return self.likes.user.username

class PostComment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey('Post',models.SET_NULL,blank=True,null=True,)
    comment = models.TextField()
    parent = models.ForeignKey('self',models.SET_NULL,blank=True,null=True,)
    timestamp = models.DateTimeField(default=datetime.now)

