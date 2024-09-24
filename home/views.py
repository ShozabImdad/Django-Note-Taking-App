from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.

class LogoutInterfaceView(View):
    template_name = 'home/login.html'

class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'

class HomeView(TemplateView):
    template_name = 'home/welcome.html'

class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin/login/'
