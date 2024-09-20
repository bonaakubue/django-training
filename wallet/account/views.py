from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from .forms import RegistrationForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy


# Create your views here.

class MyLoginView(LoginView):
    template_name = 'account/login.html'

class MyLogoutView(LogoutView):
    next_page = 'login'

class ProfileView(TemplateView):
    template_name = 'account/profile.html'

class RegistrationView(CreateView):
    model = User
    template_name = 'account/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('profile')