# Generated by Django 3.0.1 on 2020-02-06 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20200120_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='qty',
            field=models.IntegerField(default=0),
        ),
    ]
