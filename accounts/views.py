from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .forms import SignUpForm


# Create your views here.

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('main_page')
    template_name = 'accounts/signup.html'

class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_field_name = 'next' # default
    extra_context = {'key': 'value'}
    authentication_form = AuthenticationForm # default

class UserLogoutView(LogoutView):
    template_name = 'accounts/logout.html'
    redirect_field_name = 'next'
    extra_context = {}

class UserPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/change_password.html'
    extra_context = {}

class UserPermissions(TemplateView):
    template_name = 'accounts/custom_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Ваши разрешения'
        context['data'] = self.request.user.get_all_permissions()
        return context

