from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from graphene_django.views import GraphQLView

urlpatterns = [
    path('', views.index),
    path('mpesa', views.mpesa),

    path("graphql", GraphQLView.as_view(graphiql=True)),
    
]