from django.contrib import admin
from .models import User, Business, Api


# Register your models here.




class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name']

admin.site.register(User, UserAdmin)


class BusinessAdmin(admin.ModelAdmin):
    list_display = ['user']

admin.site.register(Business, BusinessAdmin)


class TokenAdmin(admin.ModelAdmin):
    list_display = ['live_api', 'user', 'test_api']

admin.site.register(Api, TokenAdmin)