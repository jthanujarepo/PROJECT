from django.db import models
import datetime
import os
# from .form import *


from django.core.mail import send_mail
# from .models import User
from django.contrib.auth.models import User 
from django.db.models.signals import post_save

# Create your models here.
class Categeroy(models.Model):
    Title=models.CharField(max_length=50,null=False,blank=False)
    # Image=models.CharField(max_length=5000)
    Image=models.ImageField(upload_to='static/images')
    Description=models.TextField(max_length=500,null=False,blank=False)
    Status=models.BooleanField(default=False,help_text="0-show,1-hidden  ")
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Title

class BooksProduct(models.Model):
    categeroy=models.ForeignKey(Categeroy,on_delete=models.CASCADE)
    title=models.CharField(max_length=30)
    # product_img=models.CharField(max_length=2000)
    product_img=models.ImageField(upload_to='static/images')
    Quantity=models.IntegerField(null=False,blank=False )
    original_price=models.IntegerField(null=False,blank=False )
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
    latest=models.BooleanField(default=False,help_text="0-default,1-Trending")
    def __str__(self):
        return self.title

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(BooksProduct,on_delete=models.CASCADE)
    product_qty=models.IntegerField(null=False,blank=False)
    created=models.DateTimeField(auto_now_add=True)
    
    # def __init__(self):
    #     return self.product_qty
    
    @property
    def total_cost(self):
      return self.product_qty * self.product.original_price 
    
    

class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    phone=models.IntegerField()
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    pincode=models.IntegerField()
    payment=models.IntegerField()


# class Orders(models.Model):
#     product=models.ForeignKey(BooksProduct,on_delete=models.CASCADE)   
#     uuid = models.ForeignKey(User,on_delete=models.CASCADE)
#     quantity = models.SmallIntegerField(blank=False, null=False)
#     discount = models.FloatField()
#     orderedOn = models.DateField(auto_now_add=True)
   
class finalorder(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Qty=models.IntegerField()
    Grand_total=models.IntegerField()
    Date=models.DateField(auto_now_add=True)
    Status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
     
def orderMsg(sender,instance,**kwargs):

            subject = "ordered Items"
            message = f'thanks for your order'
            # print(var1) 
            usermail = instance.user
            
            # message =f'%d "order" details %s'
            # plain_message=message(45,"productname")
        
            html_message=f'<h2 style="text-align:center;">Hello <span style="font-size:20px;color:teal;">{instance.user}</span></h2></br><h3 style="color:orange;font-size:20px">Thanks for Your purchase and items are </h3></br><table border="2" cellspacing="5px" cellpadding="10px" style="margin:20px auto;border-color:aqua;width:600px;heigth:500px;"><tr style="font-size:20px;color:tomato"><th>UserId</th><th>Quantity</th><th>Total</th></tr><tr style="font-size:20px;color:blue"><th>{instance.user_id}</th><th>{instance.Qty}</th><th>{instance.Grand_total}</th></tr><tr style="font-size:20px;color:tomato"><td colspan=2>Grand Total</th><th style="color:blue">{instance.Grand_total}</th></tr></table>'
    
            # print(usermail.email)
            print(instance.Qty)

            
            send_mail(subject,message,'jthanuja4@gmail.com',[usermail.email],
                    fail_silently=False,html_message= html_message) 
            # send_mail(subject,message, 'jthanuja4@gmail.com',[email],
            #         fail_silently=False,) 
post_save.connect(orderMsg,sender=finalorder) 



# class placeorder(models.Model):
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     Qty=models.IntegerField()
#     GrandTotal=models.IntegerField()
#     ordered_on=models.DateField(auto_now_add=True)
#     status=models.BooleanField(help_text="0-show ,1-hidden",default=False)

class contact(models.Model):
    Name=models.CharField(max_length=20,)
    Email=models.EmailField(max_length=20)
    Subject=models.CharField(max_length=40)
    Message=models.TextField()


from django.db import models

# class RecordDetails(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     address = models.TextField()
#     city = models.CharField(max_length=50)
#     mobile = models.CharField(max_length=15)

#     total_amount = models.IntegerField()
#     order_date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name
