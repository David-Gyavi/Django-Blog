from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import Profile

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, 
    help_text='100 characters max', required=False)
    last_name = forms.CharField(max_length=100, 
    help_text='100 characters max', required=False)
    email = forms.CharField(required=False, 
    help_text='A valid email address, please.')
    password1 = forms.CharField(label='Enter password', 
    widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', 
    widget=forms.PasswordInput)
    


    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        help_texts = {
            'username' : None,
        }


class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100, help_text='100 characters max', required=False)
    last_name = forms.CharField(max_length=100, help_text='100 characters max', required=False)
    email = forms.CharField(required=False)


    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
        help_texts = {
            'username' : None,
        }  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)   
        self.fields['username'].required = False     


class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model =  Profile
        fields = ['profile_pic']      