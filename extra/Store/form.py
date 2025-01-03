from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login,logout
from .models import *

class SignupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']


class fictionForm(forms.ModelForm):
    class Meta:
        model=fiction
        fields="__all__"


class Loginform(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']


class addbooks(forms.ModelForm):
    class Meta:
        model=Books
        exclude=['update_on']

# class bookdetailsform(forms.ModelForm):
#     class Meta:
#         model=Bookdetails
#         fields='__all__'

class contactform(forms.ModelForm):
    class Meta:
        model=contact
        fields="__all__"

class bookimageform(forms.ModelForm):
    class Meta:
        model=bookimage
        fields="__all__"
