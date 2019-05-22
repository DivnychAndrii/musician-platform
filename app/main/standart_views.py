from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.core.mail import send_mail
from rest_framework.utils import json

from main.forms import UserRegisterForm, SignUpForm


class HomePage(View):
    template = 'home.html'

    def get(self, request):
        return render(request, self.template, )


def signup(request):
    if request.method == 'POST':
        # raise ValueError(form.data)
        form = UserRegisterForm(data=request.POST.data)
        if form.is_valid():
            user = form.save()
            user.is_active = True
            user.save()

            return HttpResponse(json.dumps({"message": "Success"}),content_type="application/json")
        else:
           return HttpResponse(json.dumps({"message":form.errors}),content_type="application/json")

    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})


def logout(request):
    logout(request)
