from django.urls import path, include

from . import views

urlpatterns = [

    #path('transaction', views.transaction, name='transaction'),
    path('api/', views.api, name='api'),
    path("transaction/", views.TransactionListView.as_view(), name="transaction"),
    path('', views.index, name='index'),
    path('active', views.active_account, name='active'),

]
