# Generated by Django 3.1.4 on 2021-01-08 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='slug',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
