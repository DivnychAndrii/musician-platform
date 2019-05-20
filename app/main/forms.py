from django import forms
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
