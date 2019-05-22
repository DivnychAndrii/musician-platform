from django import forms
from django.contrib.auth.forms import UserCreationForm

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

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        password = self.cleaned_data["password"]
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ( 'name', 'email', 'password')
