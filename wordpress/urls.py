from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from graphene_django.views import GraphQLView

urlpatterns = [
    path('mpesa', views.mpesa),
    path('sandbox', views.sandbox),
    path('price', views.price, name="price"),

    path("graphql", GraphQLView.as_view(graphiql=True)),

]