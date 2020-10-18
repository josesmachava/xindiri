import json
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Transaction
from .serializers import TransactionSerializer
from mpesa.api import APIContext, APIMethodType, APIRequest
from django.http import HttpResponse, HttpResponseRedirect
from pprint import pprint
from django.http import JsonResponse
from django.urls import reverse
import secrets
# Api import End

def price(request):
    return render(request, 'wordpress/price.html')


@api_view(['GET', 'POST'])
def mpesa(request):
    """
    List all code Payment, or create a new Payment.
    """
    if request.method == 'GET':
        payments = Transaction.objects.all()
        serializer = TransactionSerializer(payments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            request_payment = request.data
            phone_number = str(258) + str(request_payment["phone_number"])
            amount = request_payment["amount"]
            website = request_payment["website"]

            reference = secrets.token_hex(6)
            api_key = request_payment["api_key"]
            public_key = request_payment["public_key"]
            service_provider = request_payment["service_provider"]
            api_context = APIContext()
            api_context.api_key = api_key
            api_context.public_key = public_key
            api_context.ssl = True
            api_context.method_type = APIMethodType.POST

            if 1 == 1:
                api_context.address = 'api.vm.co.mz'

            api_context.port = 18352
            api_context.path = '/ipg/v1x/c2bPayment/singleStage/'
            api_context.add_header('Origin', '*')
            api_context.add_parameter('input_ThirdPartyReference', '111PA2D')
            api_context.add_parameter('input_ServiceProviderCode', service_provider)
            api_context.add_parameter('input_Amount', amount)
            api_context.add_parameter('input_CustomerMSISDN', phone_number)
            api_context.add_parameter('input_TransactionReference', reference)

            api_request = APIRequest(api_context)
            result = json.dumps(api_request.execute())
            data = json.loads(result)
            print(data)

            transaction_status_code = data["status_code"]
            transaction_id = data["body"]["output_TransactionID"]
            transaction_status = data["body"]["output_ResponseDesc"]

            xpay_mpesa = Transaction(
                mpesaReturn=data,
                amount=amount,
                phone_number=phone_number,
                transaction_status_code=transaction_status_code,
                transaction_status=transaction_status,
                transaction_id=transaction_id,
                public_key=public_key,
                api_key=api_key,
                website=website,
                reference=reference)
            xpay_mpesa.save()
            format_data = {"phone_number": phone_number,
                           "amount": amount,
                           "reference": reference,
                           "transaction_id": transaction_id,
                           "transaction_status_code": transaction_status_code,
                           "transaction_status": transaction_status,
                           "api_key": api_key,
                           "website": website,

                           }
            dump = json.dumps(format_data)
            return HttpResponse(dump, content_type='application/json')

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'POST'])
def sandbox(request):
    """
    List all code Payment, or create a new Payment.
    """
    if request.method == 'GET':
        payments = Transaction.objects.all()
        serializer = TransactionSerializer(payments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            request_payment = request.data
            phone_number = str(258) + str(request_payment["phone_number"])
            amount = request_payment["amount"]
            reference = secrets.token_hex(6)
            api_key = request_payment["api_key"]
            website = request_payment["website"]
            public_key = request_payment["public_key"]
            service_provider = request_payment["service_provider"]
            api_context = APIContext()
            api_context.api_key = api_key
            api_context.public_key = public_key
            api_context.ssl = True
            api_context.method_type = APIMethodType.POST

            if 1 == 1:
                api_context.address = 'api.sandbox.vm.co.mz'

            api_context.port = 18352
            api_context.path = '/ipg/v1x/c2bPayment/singleStage/'
            api_context.add_header('Origin', '*')
            api_context.add_parameter('input_ThirdPartyReference', '111PA2D')
            api_context.add_parameter('input_Amount', amount)
            api_context.add_parameter('input_CustomerMSISDN', phone_number)
            api_context.add_parameter('input_ServiceProviderCode', service_provider)
            api_context.add_parameter('input_TransactionReference', reference)

            api_request = APIRequest(api_context)
            result = json.dumps(api_request.execute())
            data = json.loads(result)
            print(data)

            transaction_status_code = data["status_code"]
            transaction_id = data["body"]["output_TransactionID"]
            transaction_status = data["body"]["output_ResponseDesc"]

            xpay_mpesa = Transaction(
                mpesaReturn=data,
                amount=amount,
                phone_number=phone_number,
                transaction_status_code=transaction_status_code,
                transaction_status=transaction_status,
                transaction_id=transaction_id,
                public_key=public_key, api_key=api_key, reference=reference,
                website=website
            )
            xpay_mpesa.save()
            format_data = {"phone_number": phone_number,
                           "amount": amount,
                           "reference": reference,
                           "transaction_id": transaction_id,
                           "transaction_status_code": transaction_status_code,
                           "transaction_status": transaction_status,
                           "api_key": api_key,
                           "website": website

                           }
            dump = json.dumps(format_data)
            return HttpResponse(dump, content_type='application/json')

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
