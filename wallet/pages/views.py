from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'index.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class RegisterView(TemplateView):
    template_name = 'register.html'

class LoginView(TemplateView):
    template_name = 'login.html'