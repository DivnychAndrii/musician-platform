from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.views import View
from django.core.mail import send_mail, EmailMessage
from rest_framework.utils import json

from main.forms import UserRegisterForm, LoginForm


class HomePage(View):
    template = 'home.html'

    def get(self, request):
        return render(request, self.template, )


class Register(View):
    template = 'register.html'

    def get(self, request):
        return render(request, 'register.html')


class Login(View):
    template = 'login.html'

    def get(self, request):
        return render(request, 'login.html')

def logout(request):
    logout(request)
