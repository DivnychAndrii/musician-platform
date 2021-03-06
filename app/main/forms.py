from django import forms

from .models import User


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Email address')
    username = forms.CharField(label='username')
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = [
            'email',
            'password',
            'username'
        ]


class LoginForm(forms.ModelForm):
    email = forms.EmailField(label='Email address')
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = [
            'email',
            'password',
        ]
