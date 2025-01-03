from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms
from django.contrib.auth.models import User

class Customuserform(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Enter your name"}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Enter your email"}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':"Enter password"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':"Enter password"}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class Orderform(forms.ModelForm):
    class Meta:
        model=finalorder  
        fields="__all__"


class contactform(forms.ModelForm):
    class Meta:
        model=contact
        fields="__all__"
