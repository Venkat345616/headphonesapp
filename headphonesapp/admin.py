from django.contrib import admin
from . models import products
from headphonesapp.models import myUser
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin




# Register your models here.



admin.site.register(products)

class myUserInline(admin.StackedInline):
    model = myUser
    can_delete = False
    verbose_name_plural = 'myUsers'


class CustomizedUserAdmin(UserAdmin):
    inlines = (myUserInline, )




admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)
admin.site.register(myUser)

