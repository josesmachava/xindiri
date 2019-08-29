

from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [

    path('', views.phone_number, name='phone_number'),
    path('mpesaClient/', views.Mpesa, name='mpesa'),


   

]
