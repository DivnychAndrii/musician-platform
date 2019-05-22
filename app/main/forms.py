from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Email address')
    username = forms.CharField(label='username')
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'email',
            'password',
            'username'
        ]


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ( 'name', 'email', 'password')
