# Generated by Django 3.1.4 on 2021-01-12 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_order_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='products',
        ),
    ]