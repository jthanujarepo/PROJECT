from django.db import models
from django.contrib.auth import authenticate ,login,logout
from django.contrib.auth.models import User, AbstractUser
from django.forms import BaseModelForm
from .models import *
from django.urls import reverse



# Create your models here.

# class BookUser(AbstractUser):
#     phone = models.CharField(max_length=10, unique=True, blank=True, null=True)
#     address=models.CharField(max_length=50, blank=True)
#     birth_date=models.DateField()

class fiction(models.Model):
    title=models.CharField(max_length=30)
    price=models.IntegerField()
    page=models.IntegerField()
    img=models.CharField(max_length=2000)
    def __str__(self):
        return self.title

class Product(models.Model):
    fiction=models.ForeignKey(fiction,on_delete=models.CASCADE)
    title=models.CharField(max_length=30)
    Author=models.CharField(max_length=30)
    product_img=models.CharField(max_length=2000)
    Quantity=models.IntegerField(null=False,blank=False )
    original_price=models.IntegerField(null=False,blank=False )
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
    def __str__(self):
        return self.title

class CustomerAddress(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.EmailField(max_length=20)
    Phone=models.IntegerField()
    DoorNO=models.IntegerField()
    Town=models.CharField(max_length=50)
    State=models.CharField(max_length=50)
    Pincode=models.IntegerField()
    # AccountNo=models.IntegerField()
    # TransactionId=models.IntegerField()

class login(models.Model):
    username=models.CharField(max_length=20)
    password=models.IntegerField()

class Books(models.Model):
    title = models.CharField(max_length=75,blank=False, null=False)
    description=models.TextField(max_length=500)
    no_of_pages = models.IntegerField(null=False,blank=False)
    price = models.FloatField(null=False, blank=False)
    # cover_pagenew=models.ImageField(upload_to="static/images/")
    image=models.ImageField(upload_to="static/images/")
    update_on = models.DateField(auto_now_add=True)


class Bookdetails(models.Model):
     title = models.CharField(max_length=75,blank=False, null=False)
     description=models.TextField(max_length=500)
     pages=models.IntegerField(null=False,blank=False)
     price = models.FloatField(null=False, blank=False)
     image=models.CharField(max_length=3000)
     





class contact(models.Model):
    Name=models.CharField(max_length=20,)
    Email=models.EmailField(max_length=20)
    Subject=models.CharField(max_length=40)
    Message=models.TextField()

class bookimage(models.Model):
    name= models.CharField(max_length=75,blank=False, null=False)
    new_image=models.ImageField(upload_to='static/images/')

