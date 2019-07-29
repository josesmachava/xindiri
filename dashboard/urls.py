from django.urls import path, include

from . import views

urlpatterns = [

    path('', views.index, name='dashboard'),
    path('token/', views.token, name='token'),

]
