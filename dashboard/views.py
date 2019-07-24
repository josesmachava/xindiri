from django.shortcuts import render

# from account.models import User
from mpesa.models import payment
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required()
def index(request):
    paymentByUser = payment.objects.all()
    return render(request, 'dashboard/index.html',{'payments': paymentByUser})
