from django.contrib.auth.forms import UserCreationForm
from comp_app.models import CustomUser
from django import forms

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = CustomUser
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'password1',
            'password2'
        ]