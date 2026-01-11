"""Demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# from Store.views import FictionAPI, BooksView,home,about,booksdelete,BookView,BookView2,SignupView ,booksupdate,loginview,get_book,get_fiction,fictionview,contactview,home1,log_out,product
# from Store.views import *
# from Store.urls import *
# import routers 
from rest_framework import routers
rout = routers.DefaultRouter()
# rout.register(r'bookapi',BooksView)

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Booksapp.urls') ),
    # path('',include('Store.urls')),
    # path('home1/',view=home1),
    # path('about/',view=about),
    # path('logout',view=log_out),
    # path('fiction/',view=fictionview),
    # path('fictionlist/<str:fictionid>',get_fiction,name="fictiondata"),
    # path('fictionlist/',get_fiction),
    
    # path('bookimage/',view=bookimage),



 

    path('user-auth/',include('rest_framework.urls')),
    # path("",include(rout.urls)),
    
    # path("",include('Cart.urls')),   #used when urls.py is in Store
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
