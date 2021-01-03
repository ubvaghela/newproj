from django.db import models
from django.contrib.auth.models import User
from datetime import datetime 

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=250)
    author=models.ForeignKey(User,on_delete=models.CASCADE,default='ullash')
    content = models.TextField()
    created=models.DateTimeField(default=datetime.now)
    updated=models.DateTimeField(default=datetime.now)

    class Meta:
        ordering = ['-id']
    
