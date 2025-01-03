from django.contrib import admin
from .models import *
# from .views import *
 # Register your models here.

admin.site.register(Books)
admin.site.register(fiction)
admin.site.register(Product)
admin.site.register(bookimage)

