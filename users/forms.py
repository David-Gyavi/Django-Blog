from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='100 characters max.')
    last_name = forms.CharField(max_length=100, help_text='100 characters max.')
    email = forms.CharField(help_text='A valid email address, please.')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']