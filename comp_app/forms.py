from django import forms
from .models import Computer


class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ['title', 'info', 'price', 'image']

