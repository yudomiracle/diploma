# Generated by Django 5.0.1 on 2024-02-24 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comp_app', '0006_remove_cart_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]