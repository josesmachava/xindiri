
import secrets
import json
import requests
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import PaymentForm
from django_rq import job


# Create your views here.
from .models import Package, Order


@login_required()
@job('high')
def mpesa(request, pk):
    package = Package.objects.get(pk=pk)
    if request.method == "POST":

        form = PaymentForm(request.POST)
        if form.is_valid():
            número_de_telefone = request.POST['número_de_telefone']
            order = Order.objects.create(user=request.user, ordered=False, package=package)
            payment = form.save(commit=False)
            payment.user = request.user
            payment.order = order

            API_ENDPOINT = "https://development-xindiri.herokuapp.com/v1/payments/"
            data = {

                'phone_number': payment.número_de_telefone,
                'amount': package.price
                'api_key': 'a0a9fe0bf9178657835ab0ad4b033f9f',
            }
            # sending post request and saving response as response object
            payment_data = requests.post(url=API_ENDPOINT, data=data)


            response = json.loads(payment_data.text)
            print(response)
            print(response)
            status_code = response['transaction_status_code']

            if status_code == 201 or status_code == 200:
                payment.order.ordered = True
                request.user.is_business = True
                request.user.save()
                print(payment.order.pk)
                print(payment.order.ordered)
                payment.save()

                return redirect('index')

            else:
                error_message = response["transaction_status"]

                messages.error(request, error_message)

                form = PaymentForm()

        #  return redirect('post_detail', pk=post.pk)
    else:
        form = PaymentForm()

    return render(request, 'payment/payment.html', {
        'package': package,
        'form': form})




mpesa.delay()
























