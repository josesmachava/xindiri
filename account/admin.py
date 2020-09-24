from django.contrib import admin
from .models import User, Business, Token

# Register your models here.




class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name']

admin.site.register(User, UserAdmin)


class BusinessAdmin(admin.ModelAdmin):
    list_display = ['user']

admin.site.register(Business, BusinessAdmin)


class TokenAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']

admin.site.register(Token, TokenAdmin)