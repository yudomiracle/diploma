# Generated by Django 5.0.1 on 2024-02-24 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comp_app', '0007_cart_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='quantity',
        ),
    ]
