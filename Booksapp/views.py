from xml.dom.minidom import Document
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate ,login,logout
import json
from django.db.models.signals import post_save
from .models import *
from django.contrib import messages
from .form import *
from django.core.mail import send_mail
from django.contrib import messages
from django.core.mail.message import EmailMessage
from django.conf import settings
# from rest_framework import  status     #
import random as r



# Create your views here.
# def new(request):
#     order=finalorder.objects.filter(user=request.user)
#     # print(order.Qty)
#     userorder = finalorder()
#     userdetails = User.objects.get(username=request.user)
#     userorder.user=userdetails
#     # userorder.Qty = qty
#     print("khohikji",userorder.user)
#     return render(request,"new/productmsg.html",{"status":True,"order":order})

def main(request):
    products=BooksProduct.objects.filter(latest=1)
    return render(request,"new/Main.html",{"products":products})
                   
def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"logged out successfully")
    return redirect("/main")

def login_page(request):
    if request.user.is_authenticated:
        return redirect("/main")
    else:
        if request.method=="POST":
            name=request.POST.get('username')
            pwd=request.POST.get('password')
            user=authenticate(request,username=name,password=pwd)
            if user is not None:
                login(request,user)
        
                # return redirect("/home")
                return redirect("/main")
            else:
                messages.error(request,"invalid username")
                return redirect("/loginuser")
        return render(request,"new/loginnew.html")

# def userview(request): 
#     form=Customuserform()
#     if request.method=="POST":
#         form=Customuserform(request.POST)
#         if form.is_valid():
#            username=request.POST['username']
#            email=request.POST['email']
#         #    otp=""
#         #    for i in range(4):
#         #       otp+=str(r.randint(1,9))
          
#         #    print ("Your One Time Password is ")
#         #    print (otp)
#            subject = "Registration success"
#         #    message = f'hi {username} welcome to online bookstore and ur otp is '+str(otp)
#            message = f'hi {username} welcome to online bookstore  '
           
          
#         #    form.save()
#         #    mail_status=None
#            mail_status=send_mail(subject,message, 'jthanuja4@gmail.com',[email],
#             fail_silently=False,) 
#            form.save()
        
#            if bool(mail_status):
#                 # return render(request,"contact.html",{"mail":True,"obj":form})
#                 messages.success(request,"Registration success you can now login ")
#                 return redirect('login')
#            else:
#                 return render(request,"contact.html",{"mail":False,"status":True,"obj":form})
           
#         # form.save()
#         # messages.success(request,"Registration success you can now login welcome")
#         # return redirect('/loginuser')
        
   
       
#     # return render(request,"otphtml.html",{"otp":otp,"status":True})
    
#     return render(request,'new/register.html',{"form":form})
    


def userview(request):
    form = Customuserform()
    if request.method == "POST":
        form = Customuserform(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']

            subject = "Registration success"
            message = f"Hi {username}, welcome to online bookstore"

            try:
                mail_status = send_mail(
                    subject,
                    message,
                    'jthanuja4@gmail.com',
                    [email],
                    fail_silently=False,
                )
            except Exception as e:
                print("Email error:", e)
                mail_status = False

            form.save()

            messages.success(
                request,
                "Registration successful. You can now login."
            )
            return redirect('login')

    return render(request, 'new/register.html', {"form": form})    
        
def collections(request):
    categeroy=Categeroy.objects.filter(Status=0)
    return render(request,"new/collections.html",{"categeroy":categeroy})

def collectionsview(request,title):
    if(Categeroy.objects.filter(Title=title,Status=0)):
        products=BooksProduct.objects.filter(categeroy__Title=title)
        return render(request, "new/index.html" ,{"products":products,"categeroy_title":title})
    else:
        messages.warning(request,"No such Categeroy found")
        return redirect('collections')

def product_details(request,ctitle,ptitle):
    if(Categeroy.objects.filter(Title=ctitle,Status=0)):
       if(BooksProduct.objects.filter(title=ptitle,status=0)):
           products=BooksProduct.objects.filter(title=ptitle,status=0).first()
           return render(request,"new/product_details.html",{"products":products})   
       else:
            messages.error(request,"No such product found")
            return redirect('collections')
    else:
         messages.error(request,"no such categeroy found nnn")
         return redirect('collections')
    
def add_to_cart(request):
    if request.headers.get('x-requested-with')=='XMLHttpRequest':
        if request.user.is_authenticated:
            data=json.load(request)
            # print(data['product_qty'])
            # print(data['pid'])
            # print(request.user.id)
            product_qty=data['product_qty']
            product_id=data['pid']
            product_status=BooksProduct.objects.get(id=product_id)
            if product_status:
                if Cart.objects.filter(user=request.user,product_id=product_id):
                   return JsonResponse({'status':'product already in cart '},status=200)
                else:
                    if product_status.Quantity>=product_qty:
                        Cart.objects.create(user=request.user,product_id=product_id,product_qty=product_qty)
                        return JsonResponse({'status':'product added to cart'},status=200)    
                    else:   
                        return JsonResponse({'status':'Please check the quantity below and then add the quantity according to it'},status=200)

        else:
           return JsonResponse({'status':'login to add cart'},status=200)
    else:
        return JsonResponse({'status':'Invalid access'},status=200)


def cart_page(request):
    if request.user.is_authenticated:
        cart=Cart.objects.filter(user=request.user)
        amount=0;
        for x in cart:
            amount = amount + x.product.original_price * x.product_qty
        # print(amount)
        return render(request,"new/cart.html",{"status":True,"cart":cart,"amount":amount})
        
    else:
        messages.warning(request,"Your cart is empty")
        return render(request,"new/cart.html",{"error":True})
        # return messages.info(request,"no items found")






    
# def remove_cart(request,cid):
#     cartitem=Cart.objects.get(id=cid)
#     cartitem.delete()
#     return redirect("/cart")    

from django.shortcuts import get_object_or_404, redirect
def remove_cart(request, cid):
    cartitem = get_object_or_404(Cart, id=cid)
    cartitem.delete()
    return redirect("/cart")

# def remove_cart(request, cart_item_id):
#     cart_item = get_object_or_404(CartItem, id=cart_item_id)
#     cart_item.delete()
#     return redirect('cart')    
    
# def orderview(request):
#     order=Cart.objects.filter(user=request.user)
#     return render(request,"new/order.html" ,{"order":order})
#     # return render(request,"sample.html",{"dis":dis}) 

# def checkout(request):
#     items=Cart.objects.filter(user=request.user)
#     total_price = 0;
#     for a in items:
#         total_price = total_price + a.product.original_price * a.product_qty
#     context ={"items":items,"total_price":total_price}
#     return render(request,'new/checkout.html',context)



def orderview(request):
            # cart=Cart.objects.filter(user=request.user) 
            obj1=Cart.objects.filter(user=request.user)
            Grand_total=0;
            qty = 0
            for i in obj1:
                Grand_total += i.product.original_price *i.product_qty;
                qty+=i.product_qty

            userorder = finalorder()
            userdetails = User.objects.get(username=request.user)
            userorder.user=userdetails
            userorder.Qty = qty
            userorder.Grand_total = Grand_total
            userorder.Status = True
            # print('display') #name displayed
            context = {"odt":userorder,"obj1":obj1,"status":True}   
            if request.method=="POST":
                userorder.save()
                obj1.delete()
                return render(request,'new/checkout1.html',{"success":"order completed"})
            return render(request,'new/checkout1.html',context)




# def orderview(request):
#     book = RecordDetails.objects.filter(user=request.user)

#     if request.method == "POST":
#         RecordDetails.objects.create(
#             name=request.POST['name'],
#             email=request.POST['email'],
#             address=request.POST['address'],
#             city=request.POST['city'],
#             mobile=request.POST['mobile'],
#             total_amount=book.original_price
#         )
#         return redirect('order_success')

#     return render(request, 'new/checkout1.html', {'book': book})
   
    

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
                return render(request,"new/contact.html",{"mail":True,"obj":obj})
            else:
                return render(request,"new/contact.html",{"mail":False,"obj":obj})
        else:
            return render(request,'new/contact.html',{'cform':cform})
    except:
        return render(request,'new/contact.html',{'cform':cform,'error':True})

