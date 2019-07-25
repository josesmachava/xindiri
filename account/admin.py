from django.contrib import admin
from .models import User, Business

# Register your models here.




class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name']

admin.site.register(User, UserAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display = ['user']

admin.site.register(Business, StudentAdmin)

