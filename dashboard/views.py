from django.shortcuts import render

# from account.models import User
from mpesa.models import xpayMpesa
from django.contrib.auth.decorators import login_required


# Create your views here.

# @login_required()
def index(request):
    paymentByUser = xpayMpesa.objects.all()
    count = xpayMpesa.objects.all().count()
    context = {'count': count}
    return render(request, 'dashboard/index.html', {'payments': paymentByUser}, context)


def painel(request):
    paymentByUser = xpayMpesa.objects.all()[:5]
    count = xpayMpesa.objects.all().count()
    context = {'count': count}
    return render(request, 'dashboard/painel.html', {'payments': paymentByUser}, context)


def token(request):
    return render(request, 'dashboard/token.html')
