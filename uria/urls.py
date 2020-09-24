from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [

    path('', views.production, name='production'),
    path('sandbox', views.sandbox, name='sandbox'),

]
