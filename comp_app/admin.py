from django.contrib import admin
from .models import Computer, CustomUser

# Register your models here.
admin.site.register(Computer)
admin.site.register(CustomUser)