# Generated by Django 3.0.1 on 2020-01-17 23:37

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200118_0334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='cnthead2',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
