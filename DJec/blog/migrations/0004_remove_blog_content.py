# Generated by Django 3.0.1 on 2020-01-17 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='content',
        ),
    ]
