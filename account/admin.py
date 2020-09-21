from django.contrib import admin
from .models import User, Business, ProductionAPI, SandboxAPI

# Register your models here.




class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name']

admin.site.register(User, UserAdmin)


class BusinessAdmin(admin.ModelAdmin):
    list_display = ['user', 'public_key']

admin.site.register(Business, BusinessAdmin)


class ProductionAPIAdmin(admin.ModelAdmin):
    list_display = ['api_key', 'user']

admin.site.register(ProductionAPI, ProductionAPIAdmin)

class SandboxAPIAdmin(admin.ModelAdmin):
    list_display = ['api_key', 'user']

admin.site.register(SandboxAPI, SandboxAPIAdmin)