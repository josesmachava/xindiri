import json
import calendar
import requests
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime 
from django.utils.timezone import localtime, now
from datetime import timedelta
from django.contrib.auth.decorators import login_required
from pprint import pprint
from django.http import JsonResponse
from django.urls import reverse
from django.views import View





#@login_required()
def phone_number(request):
    
    return render(request, 'payment/payment.html')


#@login_required()
def mpesa(request):
    if request.method == "POST":
        response = requests.get('http://localhost:8000/payment/')
        print(response)
        pay = response.json()
        contact = str(258) + str(request.POST['contact'])
        if contact != "258":
            # Info  about our credentials Mpesa

            amount = '122'
            reference = 1235
            api_key = '9njrbcqty9ew3cyx4s6k7jvtab134rr6'
            public_key = 'MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAmptSWqV7cGUUJJhUBxsMLonux24u+FoTlrb+4Kgc6092JIszmI1QUoMohaDDXSVueXx6IXwYGsjjWY32HGXj1iQhkALXfObJ4DqXn5h6E8y5/xQYNAyd5bpN5Z8r892B6toGzZQVB7qtebH4apDjmvTi5FGZVjVYxalyyQkj4uQbbRQjgCkubSi45Xl4CGtLqZztsKssWz3mcKncgTnq3DHGYYEYiKq0xIj100LGbnvNz20Sgqmw/cH+Bua4GJsWYLEqf/h/yiMgiBbxFxsnwZl0im5vXDlwKPw+QnO2fscDhxZFAwV06bgG0oEoWm9FnjMsfvwm0rUNYFlZ+TOtCEhmhtFp+Tsx9jPCuOd5h2emGdSKD8A6jtwhNa7oQ8RtLEEqwAn44orENa1ibOkxMiiiFpmmJkwgZPOG/zMCjXIrrhDWTDUOZaPx/lEQoInJoE2i43VN/HTGCCw8dKQAwg0jsEXau5ixD0GUothqvuX3B9taoeoFAIvUPEq35YulprMM7ThdKodSHvhnwKG82dCsodRwY428kg2xM/UjiTENog4B6zzZfPhMxFlOSFX4MnrqkAS+8Jamhy1GgoHkEMrsT5+/ofjCx0HjKbT5NuA2V/lmzgJLl3jIERadLzuTYnKGWxVJcGLkWXlEPYLbiaKzbJb2sYxt+Kt5OxQqC1MCAwEAAQ=='

            pay["reference"] =  reference
            pay["api_key"] = api_key
            pay["public_key"] = public_key
            pay["contact"] = contact
            pay["amount"] = amount

            
   

