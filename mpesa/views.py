import json
from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import xpayMpesa
from .serializers import xpayMpesaSerializer
from mpesa.api import APIContext, APIMethodType, APIRequest
from django.http import HttpResponse, HttpResponseRedirect
from pprint import pprint
from django.http import JsonResponse
from django.urls import reverse


# Api import End

def index(request):
    return render(request, 'index.html')




@api_view(['GET', 'POST'])
def xpay_mpesa(request):
    """
    List all code Payment, or create a new Payment.
    """
    if request.method == 'GET':
        payments = xpayMpesa.objects.all()
        serializer = xpayMpesaSerializer(payments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = xpayMpesaSerializer(data=request.data)
        if serializer.is_valid():
            
            #Recuperando dados enviados atraves do API e criacao de variaveis
            requestPayment = request.data
            contact = str(258) + str(requestPayment["contact"])
            amount = requestPayment["amount"] 
            reference = requestPayment["reference"]
            api_key = '9njrbcqty9ew3cyx4s6k7jvtab134rr6'
            public_key = 'MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAmptSWqV7cGUUJJhUBxsMLonux24u+FoTlrb+4Kgc6092JIszmI1QUoMohaDDXSVueXx6IXwYGsjjWY32HGXj1iQhkALXfObJ4DqXn5h6E8y5/xQYNAyd5bpN5Z8r892B6toGzZQVB7qtebH4apDjmvTi5FGZVjVYxalyyQkj4uQbbRQjgCkubSi45Xl4CGtLqZztsKssWz3mcKncgTnq3DHGYYEYiKq0xIj100LGbnvNz20Sgqmw/cH+Bua4GJsWYLEqf/h/yiMgiBbxFxsnwZl0im5vXDlwKPw+QnO2fscDhxZFAwV06bgG0oEoWm9FnjMsfvwm0rUNYFlZ+TOtCEhmhtFp+Tsx9jPCuOd5h2emGdSKD8A6jtwhNa7oQ8RtLEEqwAn44orENa1ibOkxMiiiFpmmJkwgZPOG/zMCjXIrrhDWTDUOZaPx/lEQoInJoE2i43VN/HTGCCw8dKQAwg0jsEXau5ixD0GUothqvuX3B9taoeoFAIvUPEq35YulprMM7ThdKodSHvhnwKG82dCsodRwY428kg2xM/UjiTENog4B6zzZfPhMxFlOSFX4MnrqkAS+8Jamhy1GgoHkEMrsT5+/ofjCx0HjKbT5NuA2V/lmzgJLl3jIERadLzuTYnKGWxVJcGLkWXlEPYLbiaKzbJb2sYxt+Kt5OxQqC1MCAwEAAQ=='


            #Configurando informacao do API MPESA 
            api_context = APIContext()
            api_context.api_key = api_key
            api_context.public_key = public_key
            api_context.add_parameter('input_Amount', amount)
            api_context.add_parameter('input_CustomerMSISDN', contact)
            api_context.add_parameter('input_TransactionReference', reference)

            #Configuacoes Do Mpesa
            api_context.ssl = True
            api_context.method_type = APIMethodType.POST
            api_context.address = 'api.sandbox.vm.co.mz'
            api_context.port = 18346
            api_context.path = '/ipg/v1/c2bpayment/'
            api_context.add_header('Origin', '*')
            api_context.add_parameter('input_ThirdPartyReference', '8e090ace-e41b-4606-b320-0286a0b388da')
            api_context.add_parameter('input_ServiceProviderCode', '171717')
            api_request = APIRequest(api_context)


            #Enviado dados para API do MPESA
            result = json.dumps(api_request.execute())

            #Recuperando a resposta do API do MPESA
            data = json.loads(result)

            transaction_status_code = data["status_code"]
            transaction_id = data["body"]["output_TransactionID"]
            transaction_status = data["body"]["output_ResponseDesc"]

            xpay_mpesa = xpayMpesa(
                            mpesaReturn=data,
                            amount=amount,
                            contact=contact,
                            transaction_status_code=transaction_status_code,
                            transaction_status=transaction_status,
                            transaction_id=transaction_id,
                            public_key=public_key, api_key=api_key, reference=reference)
            xpay_mpesa.save()
            return Response({'data': data})


        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


