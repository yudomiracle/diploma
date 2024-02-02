from django import forms
from .models import Computer

class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ['title', 'info', 'price', 'image']

class OrderForm(forms.Form):
    products = forms.ModelMultipleChoiceField(
        queryset=Computer.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Выберите компьютеры',
    )
    quantity = forms.IntegerField(min_value=1, label='Количество')