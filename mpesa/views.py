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


# Api import End

def index(request):
    return render(request, 'index.html')


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
            requestPayment = request.data
            phone_number = str(258) + str(requestPayment["phone_number"])
            amount = requestPayment["amount"]

            reference = requestPayment["reference"]
            api_key = "s6yjzvxgkqydsuxgelwhw6txdyzqavor"
            public_key = "MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAyrOP7fgXIJgJyp6nP/Vtlu8kW94Qu+gJjfMaTNOSd/mQJChqXiMWsZPH8uOoZGeR/9m7Y8vAU83D96usXUaKoDYiVmxoMBkfmw8DJAtHHt/8LWDdoAS/kpXyZJ5dt19Pv+rTApcjg7AoGczT+yIU7xp4Ku23EqQz70V5Rud+Qgerf6So28Pt3qZ9hxgUA6lgF7OjoYOIAKPqg07pHp2eOp4P6oQW8oXsS+cQkaPVo3nM1f+fctFGQtgLJ0y5VG61ZiWWWFMOjYFkBSbNOyJpQVcMKPcfdDRKq+9r5DFLtFGztPYIAovBm3a1Q6XYDkGYZWtnD8mDJxgEiHWCzog0wZqJtfNREnLf1g2ZOanTDcrEFzsnP2MQwIatV8M6q/fYrh5WejlNm4ujnKUVbnPMYH0wcbXQifSDhg2jcnRLHh9CF9iabkxAzjbYkaG1qa4zG+bCidLCRe0cEQvt0+/lQ40yESvpWF60omTy1dLSd10gl2//0v4IMjLMn9tgxhPp9c+C2Aw7x2Yjx3GquSYhU6IL41lrURwDuCQpg3F30QwIHgy1D8xIfQzno3XywiiUvoq4YfCkN9WiyKz0btD6ZX02RRK6DrXTFefeKjWf0RHREHlfwkhesZ4X168Lxe9iCWjP2d0xUB+lr10835ZUpYYIr4Gon9NTjkoOGwFyS5ECAwEAAQ=="
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
            api_context.add_parameter('input_ServiceProviderCode', '171717')
            api_context.add_parameter('input_Amount', amount)
            api_context.add_parameter('input_CustomerMSISDN', phone_number)
            api_context.add_parameter('input_ServiceProviderCode', '900410')
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
                public_key=public_key, api_key=api_key, reference=reference)
            xpay_mpesa.save()
            format_data = {"phone_number": phone_number,
                           "amount": amount,
                           "reference": reference,
                           "transaction_id": transaction_id,
                           "transaction_status_code": transaction_status_code,
                           "transaction_status": transaction_status,
                           "api_key": api_key

                           }
            dump = json.dumps(format_data)
            return HttpResponse(dump, content_type='application/json')

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
