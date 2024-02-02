from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models
from django.utils import timezone


class Computer(models.Model):
    title = models.CharField(max_length=50)
    info = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='photos/')

    def __str__(self):
        return f'{self.title} - {self.price}'

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    shipping_address = models.TextField(blank=True, null=True)

    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        related_name='custom_user_groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_name='custom_user_permissions',
    )

class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Computer)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    shipping_address = models.TextField()

