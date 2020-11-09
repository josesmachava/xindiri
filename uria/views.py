import json

from django.core.serializers import get_serializer
from django.shortcuts import render
from rest_framework import generics
from django.core import serializers

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UriaTransaction
from .serializers import TransationSerializer
from account.models import Api, User
import secrets
from django.http import HttpResponse, HttpResponseRedirect
from pprint import pprint
from django.http import JsonResponse
from django.urls import reverse


@api_view(['GET', 'POST'])
def transation_list(request):
    """
    List all code Payment, or create a new Payment.
    """
    if request.method == 'GET':
        transactions = UriaTransaction.objects.all()
        serializer = TransationSerializer(transactions, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TransationSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            request_transaction = request.data

            phone_number = ""
            amount = ""
            api_key = ""

            amount = request_transaction["amount"]
            api_key = request_transaction["api_key"]
            phone_number = str(request_transaction["phone_number"])
            reference = secrets.token_hex(6)
            if Api.objects.filter(user=api_key).exists():
                user = User.objects.get(token=api_key)
                print(user.email)
                if not user.is_active and not user.is_business:
                    return Response("conta nao activa e dados  nao prenchidos")
                elif not user.is_business:
                    return Response("os dados da conta nao prenchidos")
                elif not user.is_active:
                    return Response("conta nao activa")
                elif len(phone_number) < 9:
                    return Response("o numero do telefone e menor que 8")
                elif len(phone_number) >9:
                    return Response("o numero do telefone e menor que 8")



                else:
                    transaction = Transaction(
                        phone_number=phone_number,
                        amount=amount,
                        reference=reference,
                        api_key=api_key
                    )
                    transaction.save()

            else:
                return Response("api key usado nao existe")

            import requests
            url = request.get_host()
            print(url)
            url = "http://{}/mpesa".format(url)
            json_data = {
                "phone_number": phone_number,
                "amount": amount,
                "reference": reference,
                "token": api_key

            }

            resp = requests.post(url=url, json=json_data)
            print(resp.status_code)
            print(resp.text)

            return Response(resp.text)

        else:
            return Response({'data': "token invalido"})




@api_view(['GET', 'POST'])
def sandbox(request,  *args, **kwargs):
    """
    List all code Payment, or create a new Payment.
    """
    if request.method == 'GET':
        transactions = UriaTransaction.objects.all()
        serializer = TransationSerializer(transactions, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TransationSerializer(data=request.data)
        print(serializer)

        if serializer.is_valid():
            request_transaction = request.data

            phone_number = ""
            amount = ""
            api_key = ""

            amount = request_transaction["amount"]
            api_key = request_transaction["api_key"]
            phone_number = str(request_transaction["phone_number"])
            reference = secrets.token_hex(6)
            api = Api.objects.get(test_api=api_key)
            print(api)
            user = User.objects.get(id=api.user_id)
            if api:

                print(user.email)
                if not user.is_active and not user.is_business:
                    return Response("conta nao activa e dados  nao prenchidos")
                elif not user.is_business:
                    return Response("os dados da conta nao prenchidos")
                elif not user.is_active:
                    return Response("conta nao activa")
                elif len(phone_number) < 9:
                    return Response("o numero do telefone e menor que 8")
                elif len(phone_number) >9:
                    return Response("o numero do telefone e menor que 8")



                else:
                    transaction = UriaTransaction(
                        phone_number=phone_number,
                        amount=amount,
                        reference=reference,
                        api_key=api_key,
                        user=user,
                    )
                    transaction.save()

            else:
                return Response("api key usado nao existe")

            import requests
            url = request.get_host()
            print(url)
            url = "http://{}/sandbox".format(url)


            json_data = {
                "phone_number": phone_number,
                "amount": amount,
                "reference": reference,
                "token": api_key,
                "user": user.id,

            }

            resp = requests.post(url=url, json=json_data)
            print(resp.status_code)
            print(resp.text)

            return Response(resp.text)

        else:
            return Response({'data': "api invalido"})



def handler404(request, exception):
    return render(request, 'error/404.html', status=404)

def handler500(request):
    return render(request, 'error/500.html', status=500)