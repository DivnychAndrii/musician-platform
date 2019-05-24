from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from django.views import View


class HomePage(View):
    template = 'home.html'

    def get(self, request):
        @shared_task
        def send_mail():
            title = 'Verify'
            mail_message = f'Follow this link to verify your account'
            mail = EmailMultiAlternatives(title, mail_message, to='kelurici@tech5group.com')
            mail.attach_alternative(mail_message, mimetype=mail_message)
            mail.send()
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
