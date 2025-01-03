from urllib import request
from django.db.models.signals import pre_save, post_save,pre_delete,post_delete
from django.shortcuts import render
from .models import *
from django.dispatch import receiver ,Signal
from django.core.signals import request_finished


# @receiver(request_finished)
# def fun(sender,**kwargs):
#     print("request finished")
 
# mysignal = Signal(providing_args=['name'])  ##not working

# def signaltest(sender):##
#     mysignal.send(sender=bookimage,name='surya')##
#     return render(request,'imageupdate.html')

# @receiver(mysignal)##
# def fun(sender,**kwargs):
#     print("\n\n",kwargs)
 




# def book_saved(instance,**kwargs):
#     print("data saved ",instance)
#     instance.price=500

# pre_save.connect(receiver=book_saved,sender=Books)

# @receiver(pre_save,sender=Books)
# def book_saved(self,instance,**kwargs):
#     print("data saved ",instance)
#     # instance.price=500

def login_save(sender,instance,**kwargs):  #post_save
    print("post save is working")
post_save.connect(login_save,sender=login) 


def login_presave(sender,instance,**kwargs): #pre_save
    print("pre save is working")
pre_save.connect(login_presave,sender=login) 


def login_delete(sender,instance,**kwargs):  #pre_delete
    print("pre delete is done")
pre_delete.connect(login_delete,sender=login) 


def login_postdelete(sender,instance,**kwargs):  #post_delete
    print("post is deleted")
post_delete.connect(login_postdelete,sender=login)  


def login_delete(sender,instance,**kwargs):  #post_delete for contact class
    print("post delete is successful")
post_delete.connect(login_delete,sender=contact)
    