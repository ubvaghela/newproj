from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Blog(models.Model):
	post_id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=200,default="")
	head0 = models.CharField(max_length=200,default="")
	cnthead0 = RichTextField()
	head1 = models.CharField(max_length=200,default="")
	cnthead1 = RichTextUploadingField()
	head2 = models.CharField(max_length=200,default="")
	cnthead2 = RichTextUploadingField(config_name='special')
	pub_date = models.DateField()
	thumbnail = models.ImageField(upload_to='blog/images',default='')

	def __str__(self):
		return self.title
    