from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from main.forms import UserRegisterForm


class HomePage(View):
    template = 'home.html'

    def get(self, request):
        return render(request, self.template, )


class Register(View):
    template = 'register.html'
    form = UserRegisterForm

    def get(self, request):
        form = self.form()
        context = {
            'form': form, }
        return render(request, self.template, context)

    def post(self, request):
        form = self.form(request.POST)

        if form.is_valid():
            user = form.save()
            password = form.cleaned_data.get('password')
            user.set_password(password)
            return HttpResponseRedirect(reverse('index'))

        context = {
            'form': form,
        }
        return render(request, self.template, context)
