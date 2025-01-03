from django.contrib import admin
from django.urls import path,include
# from .views import *
from . import views

urlpatterns = [

    path('emailattach',views.emailattachement ),
    path('samplemodel/',views.function),
    path('emailotp' ,views.emailotp1),
    path("otp",views.otp,name="otp"),
    # path("otpnew",views.otpgen),
    path('index2',views.index2)

]