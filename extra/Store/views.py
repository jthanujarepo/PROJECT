from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import authenticate ,login,logout
from django.core.mail import send_mail
from django.contrib import messages
from django.core.mail.message import EmailMessage
from django.conf import settings
from django.core import exceptions
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views import View
from rest_framework import viewsets, status     #
from rest_framework.response import Response    #


from rest_framework.views import APIView        #
from .form import *
from .models import *
import json     #
# import datetime
# from .serializers import BookSerializer, FictionSerializer,bookdetailserializer#
from .serializers import *


# Create your views here.

def home1(request):
    return render(request,"Home1.html")

def product(request):
    return render(request,"product.html")

def about(request):
    return render(request,"About.html")

def contactview(request):
    try:
        cform=contactform()
        if request.method=="POST":
            cform=contactform(request.POST)
            obj=contact()
            obj.Name=cform.data['Name']
            obj.Email=cform.data['Email']
            obj.Subject=cform.data['Subject']
            obj.Message=cform.data['Message']
            obj.save()
            mail_status=None
            mail_status= send_mail(obj.Subject,
            # f'{obj.Name} has send request from application {obj.Email}. message is {obj.Message}',
            # 'jthanuja4@gmail.com',['buvanesh641@gmail.com'],
            f'{obj.Name} has send request from application {obj.Email}. message is {obj.Message}',
            'buvanesh641@gmail.com',['jthanuja4@gmail.com'],
            
            fail_silently=False,
            )
            if bool(mail_status):
                return render(request,"contact.html",{"mail":True,"obj":obj})
            else:
                return render(request,"contact.html",{"mail":False,"obj":obj})
        else:
            return render(request,'contact.html',{'cform':cform})
    except:
        return render(request,'contact.html',{'cform':cform,'error':True})

def mail(request):
    sub="testing  html page"
    msg="successfully u received this message"
    to="jthanuja4@gmail.com"
    html="About.html"
    # html_message=render_to_tring(html)
    message=EmailMessage(sub,html,settings.EMAIL_HOST_USER,[to])
    message.content_subtype='html'
    message.send()
    return HttpResponse('success')






def home(request): #add books in table
    bookform=addbooks()
    if request.method=="POST":
        book = addbooks(request.POST)
        if book.is_valid():
            print(book)
            book.save()
        books = Books.objects.all()

        return render(request,"home.html",{"bookform":bookform,"books":book})
    else:
        books = Books.objects.all()
        return render(request,"home.html",{"bookform":bookform,"books":books})

        
def get_book(request,bookid):
    try:
        # b = Books.objects.get(id=bookid)
        b=Books.objects.filter(title__icontains=bookid)
        if b is not None:
            return render(request,"product.html",{"book":b})
        else:
            render(request,"product.html",{"error":"Book id is not valid"})
    except:
        return render(request,"product.html",{"error":"Book id is not valid"})


def SignupView(request):
    sform=SignupForm()
    if request.method=="POST":
        sform=SignupForm(request.POST)
        user=User()
        user.username=sform.data['username']
        user.email=sform.data['email']
        user.password=make_password(sform.data['password'])
        # user.first_name=sform.data['first_name']
        # user.last_name=sform.data['last_name']
        user.save()
        # username=user.cleaned_data.get('username')
        # print("ur account created successfully")
        messages.success(request,'Account created successfully')  
        if user is not None:
            login(request,user)
            return redirect('/login')
        else:
              return render(request,'login.html',{"status":True,'user':user})
            # return render(request,'login.html',{} )
    else:
        return render(request,'signup.html',{'sform':sform})
    



def loginview(request):
    lform=Loginform()
    # if request.user.username:
    #     return redirect("/home1")
    if request.method=="POST":
        lform=Loginform(request.POST)
        # user=User()
        user=authenticate(username=lform.data['username'], password=lform.data['password'])
        
       
        if user is not None:
                login(request,user)
                return redirect('/home1')
           
        else:
           return render(request,"login.html",{"error":True,"lform":lform})
                

    else:
        return render(request,'login.html',{'lform':lform})
   
def log_out(request):
    logout(request)
    return redirect('/login')

def fictionview(request):
    form=fictionForm()
    if request.method=="POST":
        obj=fictionForm(request.POST)
        if obj.is_valid():
            obj.save()
            objs = fiction.objects.all()
            return render(request ,"fiction.html",{"form":form,"obj":obj})
    else:
        objs =fiction.objects.all()
        return render(request,"fiction.html",{"form":form,"obj":objs})
    

def get_fiction(request,fictionid):
    try:
        b=fiction.objects.filter(title__icontains=fictionid)
        if b is not None:
            return render(request,"product.html",{"obj":b})
        else:
            render(request,"product.html",{"error":"Book id is not valid"})
    except:
        return render(request,"product.html",{"error":"Book id is not valid"})


class BookView(CreateView):
    model=Books
    fields=['title','no_of_pages','price', 'cover_page']
    template_name='books_form.html'
    success_url="/home"
    
class BookView2(ListView):
    model=Books
    fields=['title','no_of_pages','price', 'cover_page']
    template_name='books_list.html'
    success_url="/home"
    context_object_name='books'

class booksupdate(UpdateView):
    model=fiction
    fields=['price']  
    template_name= 'update_form.html'
    success_url='/fiction'


class booksdelete(DeleteView):
    model=fiction
    template_name='delete_form.html'
    context_object_name='d'   #task is a obj a name where we can the fields i.e d.title
    success_url=reverse_lazy('list')  #the page where it want to redirect after success 'list' is name


    
#CRUD Operations 
# Create, Read, Update, Delete 
# Generic View -  View class, 

# pip install django-rest-framework
# pip install markdown
# pip install django-filter

#Books View in Restframework
# add rest_framework in settings
# create model serializers
# create view with modelviewset
# add routers 3.
# add the routers in urls'

class BooksView(viewsets.ModelViewSet):
    queryset=Books.objects.all()
    serializer_class=BookSerializer

# Fiction Class based View

class FictionAPI(APIView):

    def get(self, request, pk=None, format=None):
        if pk is not None:
            fictoindata=fiction.objects.get(pk=pk)
            serialize_data = FictionSerializer(fictoindata)
            return Response(serialize_data.data,status=status.HTTP_200_OK)
        
        fictoindata=fiction.objects.all()
        serialize_data = FictionSerializer(fictoindata,many=True)
        return Response(serialize_data.data,status=status.HTTP_200_OK)

    def post(self,request,format=None):
        try:
            serializedata = FictionSerializer(data=request.data)
            if serializedata.is_valid():
                serializedata.save()
                return Response({"msg":"data saved"},status=status.HTTP_201_CREATED)
            else:
                return Response(serializedata.errors,status=status.HTTP_206_PARTIAL_CONTENT)
        except:
                return Response(serializedata.errors,status=status.HTTP_206_PARTIAL_CONTENT)


    def delete(self,request,pk, format=None):
        fictid=pk
        try:
            fictiondata = fiction.objects.get(id=fictid)
            fictiondata.delete()
            return Response({"msg":"data deleted"}, status=status.HTTP_200_OK)
        except:
            return Response({"msg":"some error occured check id"}, status=status.HTTP_204_NO_CONTENT)



# def put(self,pk,request,format=None):
#         id=pk
#         fictiondata = fiction.objects.get(pk=id)
#         serializer=FictionSerializer(fictiondata,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'text':'put method is worked'})
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        try:
            fictiondata = fiction.objects.get(pk=pk)
            serializer=FictionSerializer(fictiondata,data=request.data)
            if  serializer.is_valid():
                serializer.save()
                return Response({"status":205,'text':'success'})
            
            return Response({'text':'put method is worked'})
        except:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk):
        try:
            fictiondata = fiction.objects.get(pk=pk)
            serializer=FictionSerializer(fictiondata,data=request.data,partial=True)
            if  serializer.is_valid():
                serializer.save()
                return Response({"status":205,'text':'patch method worked successfully'})
            
            return Response({'text':'put method is worked'})
        except:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

def collections(request):
    obj1=fiction.objects.all()
    return render(request,'About.html',{"obj":obj1})

def collectionsview(request,title):
    if(fiction.objects.filter(title=title)):
    # if(fiction.objects.all()):
        products=Product.objects.filter(title=title)
        return render(request, "index.html" ,{"products":products})
    else:
        messages.warning(request,"No such Categeroy found")
        return redirect('collections')

def imageupdate(request):
    imageform= bookimageform()
    allimages = bookimage.objects.all()
    if request.method=="POST":
        imageform = bookimageform(request.POST,request.FILES)
        print(imageform['new_image'])
        if imageform.is_valid():
            imageform.save()
            print(imageform['new_image'])
            print(imageform['name'])

            allimages = bookimage.objects.all()
            return render(request,'imageupdate.html',{'msg':'image updated','img':allimages})
        return render(request,'imageupdate.html',{'form':imageform,'img':allimages})
    return render(request,'imageupdate.html',{'form':imageform,'img':allimages})
