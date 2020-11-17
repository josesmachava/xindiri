
import secrets
import json
import requests
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import PaymentForm


# Create your views here.
from .models import Package


@login_required()
def mpesa(request, pk):
    package = Package.objects.get(pk=pk)
    if request.method == "POST":

        form = PaymentForm(request.POST)
        if form.is_valid():
            número_de_telefone = request.POST['número_de_telefone']

            order = Order.objects.create(user=request.user, ordered=False, book=book)
            payment = form.save(commit=False)
            payment.user = request.user
            payment.order = order

            API_ENDPOINT = "https://xpayy.herokuapp.com/payment/"
            data = {

                'contact': payment.número_de_telefone,
                'amount': package.price,
                'api_key': 'cpurgkttk6fw317ucnnxaqxcnrkxszgs',
            }
            # sending post request and saving response as response object
            payment_data = requests.post(url=API_ENDPOINT, data=data)

            response = json.loads(payment_data.text)
            status_code = response['data']["status_code"]
            if status_code == 201 or status_code == 200:
                payment.order.ordered = True
                print(payment.order.pk)
                print(payment.order.ordered)
                payment.save()
                order.save()
                return redirect('read', pk)

            else:
                error_message = response['data']['body']["output_ResponseDesc"]

                messages.error(request, error_message)

                form = PaymentForm()

        #  return redirect('post_detail', pk=post.pk)
    else:
        form = PaymentForm()

    return render(request, 'payment/payment.html', {
        'package': package,
        'form': form})




















  







        
        