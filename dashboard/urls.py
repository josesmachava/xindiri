from django.urls import path, include

from . import views

urlpatterns = [

    path('transaction', views.transaction, name='transaction'),
    path('api/', views.api, name='api'),
    path('', views.index, name='index'),
    path('active', views.active_account, name='active'),

]
