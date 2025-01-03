from django.contrib import admin
from .models import *
# from .form import *


# class categeroyadmin(admin.ModelAdmin):
#     var=('title','img','description')
# admin.site.register(Categeroy,categeroyadmin)

# Register your models here.
admin.site.register(Categeroy)
admin.site.register(BooksProduct)
admin.site.register(Cart)
admin.site.register(finalorder)
# admin.site.register(UserCreationForm)




# admin.site.register(User)

