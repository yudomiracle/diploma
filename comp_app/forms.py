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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['quantity'].widget.attrs.update({'class': 'form-control', 'min': 1})
        self.fields['shipping_address'].widget.attrs.update({'class': 'form-control'})