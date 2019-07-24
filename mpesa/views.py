import json
from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import payment
from .serializers import PaymentSerializer

# Api import Start
from mpesa.api import APIContext, APIMethodType, APIRequest
from django.http import HttpResponse, HttpResponseRedirect
from pprint import pprint
from django.http import JsonResponse
from django.urls import reverse


# Api import End

def index(request):
    return render(request, 'index.html')




@api_view(['GET', 'POST'])
def payment_list(request):
    """
    List all code Payment, or create a new Payment.
    """
    if request.method == 'GET':
        payments = payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            requestPayment = request.data
            contact = str(258) + str(requestPayment["contact"])
            amount = requestPayment["amount"]
            phone_number = requestPayment['phone_number']
            reference = requestPayment["reference"]
            api_key = requestPayment["api_key"]
            public_key = requestPayment["public_key"]
            api_context = APIContext()
            api_context.api_key = api_key
            api_context.public_key = public_key
            api_context.ssl = True
            api_context.method_type = APIMethodType.POST

            if 1 == 1:
                api_context.address = 'api.sandbox.vm.co.mz'

            api_context.port = 18346
            api_context.path = '/ipg/v1/c2bpayment/'

            api_context.add_header('Origin', '*')

            api_context.add_parameter('input_ThirdPartyReference', '8e090ace-e41b-4606-b320-0286a0b388da')
            api_context.add_parameter('input_Amount', amount)
            api_context.add_parameter('input_CustomerMSISDN', contact)
            api_context.add_parameter('input_ServiceProviderCode', '171717')
            api_context.add_parameter('input_TransactionReference', reference)

            api_request = APIRequest(api_context)
            result = json.dumps(api_request.execute())
            data = json.loads(result)
            print(data)
            transaction_status_code = data["status_code"]
            transaction_id = data["body"]["output_TransactionID"]
            transaction_status = data["body"]["output_ResponseDesc"]
            # p_number = phone_number
            # if phone_number == "849394995":

            pay = payment(
                    mpesaReturn=data,
                    amount=amount,
                    contact=contact,
                    transaction_status_code=transaction_status_code,
                    transaction_status=transaction_status,
                    transaction_id=transaction_id,
                    public_key=public_key, api_key=api_key, reference=reference)
            pay.save()
            #     return Response({'data': data})
            # else:
            #     return Response({'data': "wrong number"})

            # return Response(serializer.data, status=status.HTTP_201_CREATED, paymts = data["status_code"] )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
