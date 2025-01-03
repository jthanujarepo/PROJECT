from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class emailotp(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Enter your name"}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Enter your email"}))
   
    class Meta:
        model=User
        fields=['username','email']
        
# class emailotp(forms.ModelForm):
#     class Meta:
#         model=User
#         fields=['username','email']