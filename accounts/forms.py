from django.contrib.auth.forms import UserCreationForm
from comp_app.models import CustomUser
from django import forms
from django.contrib.auth.forms import PasswordChangeForm

class CustomPasswordChangeForm(PasswordChangeForm):
    error_messages = {
        'password_incorrect': ("Введенный старый пароль неверен. Пожалуйста, попробуйте снова."),
        'password_mismatch': ("Введенные новые пароли не совпадают."),
        'password_too_short': ("Пароль должен содержать как минимум 8 символов."),
        'password_too_common': ("Ваш пароль слишком распространен."),
        'password_entirely_numeric': ("Пароль не может состоять полностью из цифр."),
        'password_similar_to_username': ("Ваш пароль не может быть слишком похож на ваше имя пользователя."),
    }

    field_labels = {
        'old_password': ('Старый пароль'),
        'new_password1': ('Новый пароль'),
        'new_password2': ('Подтверждение нового пароля'),
    }

    field_help_texts = {
        'old_password': ('Введите ваш текущий пароль'),
        'new_password1': ('Введите ваш новый пароль'),
        'new_password2': ('Введите ваш новый пароль еще раз для подтверждения'),
    }

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
            'shipping_address',
            'password1',
            'password2'
        ]