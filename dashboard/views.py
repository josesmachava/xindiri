from django.shortcuts import render

# from account.models import User
from mpesa.models import xpayMpesa
from django.contrib.auth.decorators import login_required


# Create your views here.

# @login_required()
def transaction(request):
    paymentByUser = xpayMpesa.objects.all()
    count = xpayMpesa.objects.all().count()
    context = {'count': count}
    return render(request, 'dashboard/transaction.html', {'payments': paymentByUser}, context)


def index(request):
    paymentByUser = xpayMpesa.objects.all()[:5]
    count = xpayMpesa.objects.all().count()
    context = {'count': count}
    return render(request, 'dashboard/index.html', {'payments': paymentByUser}, context)


def active_account(request):
    return render(request, 'dashboard/active_account.html')


def api(request):
    return render(request, 'dashboard/developer/api.html')
