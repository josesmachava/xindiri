from django.shortcuts import render
import json
import requests
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
def phone_number(request):
    
    return render(request, 'payment/payment.html')



def Mpesa(request):

      if request.method == 'POST':
           contact = str(request.POST['contact'])
           print(contact)
           amount = '248'
           reference = "r1dads"
           api_key = '9njrbcqty9ew3cyx4s6k7jvtab134rr6'
           public_key = 'MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAmptSWqV7cGUUJJhUBxsMLonux24u+FoTlrb+4Kgc6092JIszmI1QUoMohaDDXSVueXx6IXwYGsjjWY32HGXj1iQhkALXfObJ4DqXn5h6E8y5/xQYNAyd5bpN5Z8r892B6toGzZQVB7qtebH4apDjmvTi5FGZVjVYxalyyQkj4uQbbRQjgCkubSi45Xl4CGtLqZztsKssWz3mcKncgTnq3DHGYYEYiKq0xIj100LGbnvNz20Sgqmw/cH+Bua4GJsWYLEqf/h/yiMgiBbxFxsnwZl0im5vXDlwKPw+QnO2fscDhxZFAwV06bgG0oEoWm9FnjMsfvwm0rUNYFlZ+TOtCEhmhtFp+Tsx9jPCuOd5h2emGdSKD8A6jtwhNa7oQ8RtLEEqwAn44orENa1ibOkxMiiiFpmmJkwgZPOG/zMCjXIrrhDWTDUOZaPx/lEQoInJoE2i43VN/HTGCCw8dKQAwg0jsEXau5ixD0GUothqvuX3B9taoeoFAIvUPEq35YulprMM7ThdKodSHvhnwKG82dCsodRwY428kg2xM/UjiTENog4B6zzZfPhMxFlOSFX4MnrqkAS+8Jamhy1GgoHkEMrsT5+/ofjCx0HjKbT5NuA2V/lmzgJLl3jIERadLzuTYnKGWxVJcGLkWXlEPYLbiaKzbJb2sYxt+Kt5OxQqC1MCAwEAAQ=='

           url='http://localhost:8000/payment/'

           data = {
               'reference':reference,
               'api_key':api_key,
               'contact':contact,
               'amount':amount,
               'public_key':public_key,
               
  
                
       
        }  
           headers = {'content-type': 'application/json'}
 
           response = requests.post(url, data)
           
           print(response.status_code) 
           print(response) 
           return render(request, 'payment/payment.html')
    
      