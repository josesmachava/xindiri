
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

            API_ENDPOINT = "https://xpayy.herokuapp.com/payment/"
            data = {

                'contact': payment.número_de_telefone,
                'amount': "1",
                'reference': secrets.token_hex(4),
                'api_key': 'fv9209jesuwbxhneoithqo6us7rukpu4',
                'public_key': "MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAmptSWqV7cGUUJJhUBxsMLonux24u+FoTlrb+4Kgc6092JIszmI1QUoMohaDDXSVueXx6IXwYGsjjWY32HGXj1iQhkALXfObJ4DqXn5h6E8y5/xQYNAyd5bpN5Z8r892B6toGzZQVB7qtebH4apDjmvTi5FGZVjVYxalyyQkj4uQbbRQjgCkubSi45Xl4CGtLqZztsKssWz3mcKncgTnq3DHGYYEYiKq0xIj100LGbnvNz20Sgqmw/cH+Bua4GJsWYLEqf/h/yiMgiBbxFxsnwZl0im5vXDlwKPw+QnO2fscDhxZFAwV06bgG0oEoWm9FnjMsfvwm0rUNYFlZ+TOtCEhmhtFp+Tsx9jPCuOd5h2emGdSKD8A6jtwhNa7oQ8RtLEEqwAn44orENa1ibOkxMiiiFpmmJkwgZPOG/zMCjXIrrhDWTDUOZaPx/lEQoInJoE2i43VN/HTGCCw8dKQAwg0jsEXau5ixD0GUothqvuX3B9taoeoFAIvUPEq35YulprMM7ThdKodSHvhnwKG82dCsodRwY428kg2xM/UjiTENog4B6zzZfPhMxFlOSFX4MnrqkAS+8Jamhy1GgoHkEMrsT5+/ofjCx0HjKbT5NuA2V/lmzgJLl3jIERadLzuTYnKGWxVJcGLkWXlEPYLbiaKzbJb2sYxt+Kt5OxQqC1MCAwEAAQ==",
            }
            # sending post request and saving response as response object
            payment_data = requests.post(url=API_ENDPOINT, data=data)

            response = json.loads(payment_data.text)
            status_code = response['data']["status_code"]

            if status_code == 201 or status_code == 200:
                payment.order.ordered = True
                request.user.is_business = True
                request.user.save()
                payment.save()
                return redirect('index')

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



























