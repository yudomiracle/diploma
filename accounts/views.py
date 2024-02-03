from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.models import User
class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('main_page')
    template_name = 'accounts/signup.html'


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_field_name = 'next'
    extra_context = {'key': 'value'}
    authentication_form = AuthenticationForm

    def form_valid(self, form):
        response = super().form_valid(form)
        return HttpResponseRedirect(reverse('user_profile'))

def UserLogoutView(request):
    logout(request)

    return render(request, 'accounts/logout.html', {'message': 'Пользователь успешно вышел'})

class UserPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/change_password.html'
    extra_context = {}

class UserPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'accounts/password_change_done.html'
    extra_context = {}


class UserPermissions(TemplateView):
    template_name = 'accounts/custom_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Ваши разрешения'
        context['data'] = self.request.user.get_all_permissions()
        return context

def UserProfile(request):
    user = request.user

    return render(request, 'accounts/user_profile.html', {user: "user"})


