from django.core.mail import EmailMessage
from django.shortcuts import render,redirect

from rest_framework.decorators import api_view
from rest_framework.response import Response
# from Store.models import Cart,Cartitems
from .models import *
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail

import random as r
from .form import *


@api_view()
def index2(request):
     return Response({'statu':200,'message':"this is successfully executed"})
# from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.
# def booktextview(request):
#     return render()

def add(a,b):
    if type(a) in [int,float] and type(b) in [int,float]:
        return a+b
    else:
        raise ValueError('a and b must be int or float')
    
def addvalues(a,b):
    return a+b

def emailattachement(request):
    if request.method=="post":
        # file=request.FILES.get("file")
        email=EmailMessage(
            "word file",
            "python concepts",
            "jthanuja4@gmail.com",
            ["jthanuja4@gmail.com"]
        )
        file=request.FILES["file"]

        email.attach(
            file.name,
            file.read(),
            file.content_type
        )
        email.send()
        # return render(request,"contact.html")
        return HttpResponse("SENT")


def function(request):
     
     obj=samplemodel()
     obj.img="static/images/book1.jpeg"
     obj.name="book1"
     obj.no=369

     obj1=samplemodel()
     obj1.img="static/images/non3.jpg"
     obj1.name="book2"
     obj1.no=364

     obj2=samplemodel()
     obj2.img="static/images/non2.jpg"
     obj2.name="book3"
     obj2.no=345

     objs = [obj,obj1,obj2]
 
     return render(request,"sample.html",{"objs":objs})

def emailotp1(request):
    print("1")
    otpform=emailotp()

    if request.method=="POST":
            print("2")
            otpform=emailotp(request.POST)    
        # if otpform.is_valid():
        # if form1 != True:
        #     form.save()
           
            username=request.POST['username']
            email=request.POST['email']
            
            # username=form1.data['username']
            # email=form1.data['email']
            print(username)
            # v1={"username":username,"email":email,"status":False}

            otp=""
            for i in range(4):
                    otp+=str(r.randint(1,9))
            
            print ("Your One Time Password is ")
            print (otp)
            subject = "Your One Time Password is"
            message = f'hi {username} otp is '+str(otp)

            mail_status=send_mail(subject,message, 'jthanuja4@gmail.com',[email],
                                fail_silently=False,) 
            # obj4.save()
            # otpform.save()
            print("ghgjli")
            # print(username)
            # v1= {"obj":form1}       
            if bool(mail_status):
                messages.success(request,"U successfully recived otp ")
                # return redirect('/otp')
                return render(request,"emailotp.html",{"obj1":otpform})
                                            
            else:
                return render(request,"contact.html",{"mail":False,"status":True,"obj":otpform})

    print("last")
    return render(request,'emailotp.html',{"obj":otpform})


def otp(request):
    # otp=""
    # for i in range(4):
    #     otp+=str(r.randint(1,9))
    return render(request,"otphtml.html",{"status":True})

# def otpgen(request):
#     otp=""
   
#     for i in range(4):
#         otp+=str(r.randint(1,9))

#     print ("Your One Time Password is ")
#     print (otp)
#     return render(request,"otphtml.html",{"otp":otp,"status":True})
