# Generated by Django 3.0.1 on 2020-01-17 22:04

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200118_0239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='cnthead1',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
