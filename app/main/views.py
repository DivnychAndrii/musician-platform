from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.http import HttpResponseRedirect
from django import forms


def index(request):

    return render(request, "index.html",)


class UserRegistrationForm(forms.Form):
    email = forms.CharField(
        required=True,
        label='Email',
        max_length=32,
    )
    password = forms.CharField(
        required=True,
        label='Password',
        max_length=32,
        widget=forms.PasswordInput()
    )


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        user = get_user_model()
        if form.is_valid():
            user_obj = form.cleaned_data
            email = user_obj['email']
            password = user_obj['password']
            if not (user.objects.filter(email=email).exists()):
                user = authenticate(email=email, password=password)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('Looks like a username with that '
                                            'email or password already exists')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


def logout_view(request):

    logout(request)
    return render(request, 'index.html')
