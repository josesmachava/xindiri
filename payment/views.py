
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
                'amount': package.price,
                'reference': secrets.token_hex(4),
                "short_code":"900511",
                'api_key': 'q6phoogrb6feqthw6fco8i5iz2lrwipy',
                'public_key': " MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAyrOP7fgXIJgJyp6nP/Vtlu8kW94Qu+gJjfMaTNOSd/mQJChqXiMWsZPH8uOoZGeR/9m7Y8vAU83D96usXUaKoDYiVmxoMBkfmw8DJAtHHt/8LWDdoAS/kpXyZJ5dt19Pv+rTApcjg7AoGczT+yIU7xp4Ku23EqQz70V5Rud+Qgerf6So28Pt3qZ9hxgUA6lgF7OjoYOIAKPqg07pHp2eOp4P6oQW8oXsS+cQkaPVo3nM1f+fctFGQtgLJ0y5VG61ZiWWWFMOjYFkBSbNOyJpQVcMKPcfdDRKq+9r5DFLtFGztPYIAovBm3a1Q6XYDkGYZWtnD8mDJxgEiHWCzog0wZqJtfNREnLf1g2ZOanTDcrEFzsnP2MQwIatV8M6q/fYrh5WejlNm4ujnKUVbnPMYH0wcbXQifSDhg2jcnRLHh9CF9iabkxAzjbYkaG1qa4zG+bCidLCRe0cEQvt0+/lQ40yESvpWF60omTy1dLSd10gl2//0v4IMjLMn9tgxhPp9c+C2Aw7x2Yjx3GquSYhU6IL41lrURwDuCQpg3F30QwIHgy1D8xIfQzno3XywiiUvoq4YfCkN9WiyKz0btD6ZX02RRK6DrXTFefeKjWf0RHREHlfwkhesZ4X168Lxe9iCWjP2d0xUB+lr10835ZUpYYIr4Gon9NTjkoOGwFyS5ECAwEAAQ==",
            }
            # sending post request and saving response as response object
            payment_data = requests.post(url=API_ENDPOINT, data=data)

            response = json.loads(payment_data.text)
            print(response)
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



























