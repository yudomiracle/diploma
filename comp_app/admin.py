from django.contrib import admin
from .models import Computer, CustomUser, Cart

# Register your models here.
admin.site.register(Computer)
admin.site.register(CustomUser)
admin.site.register(Cart)