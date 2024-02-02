from django import forms
from .models import Computer, Order


class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ['title', 'info', 'price', 'image']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['products', 'quantity', 'shipping_address']