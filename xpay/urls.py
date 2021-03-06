"""xpay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('mpesa.urls')),
    path('pay/', include('payment.urls')),
    path('account/', include('account.urls')),
    path('django-rq/', include('django_rq.urls')),
    path('v1/payments/', include('uria.urls')),
    path('v1/wordpress/', include('wordpress.urls')),
    path('v1/send/', include('send.urls')),
    path('dashboard/', include('dashboard.urls')),

]




handler404 = "uria.views.handler404"
handler500 = "uria.views.handler500"
