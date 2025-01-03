from django.urls import path
from . import views
# from .form import *

urlpatterns = [ 
    # path('new',views.new),
    path('main/',views.main ,name='home'),
    path('register',views.userview,name='register'),
    path('loginuser',views.login_page,name='login'),
    path('logout',views.logout_page,name='logout'),
    path('cart/',views.cart_page,name='cart'),
    path('remove_cart/<str:cid>',views.remove_cart,name='remove_cart'),
    
    # path('collections1',views.collections,name="collectionsnew")
    path('collections',views.collections,name='collections'), #aboutpage new
    
    path('collections/<str:title>',views.collectionsview,name='collections'),
    # path('sampleone',views.collectionsview,name='categeroy'),

    path('collections/<str:ctitle>/<str:ptitle>',views.product_details,name='product_details'),
    path('addtocart',views.add_to_cart,name='addtocart'),
    # path('checkout',views.checkout,name='checkout1'),
    path('order1',views.orderview,name="order"),

    path('contact/',views.contactview,name='contact'),


]  