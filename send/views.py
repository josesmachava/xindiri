import json
from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import  Payment
from .serializers import  PaymentSerializer
from account.models import Token, User
import secrets
from django.http import HttpResponse, HttpResponseRedirect
from pprint import pprint
from django.http import JsonResponse
from django.urls import reverse


@api_view(['GET', 'POST'])
def send(request):
    """
    List all code Payment, or create a new Payment.
    """
    if request.method == 'GET':
        transactions = Payment.objects.all()
        serializer = PaymentSerializer(transactions, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PaymentSerializer(data=request.data)
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
            if Token.objects.filter(id=api_key).exists():
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
def sandbox(request):
    """
    List all code Payment, or create a new Payment.
    """
    if request.method == 'GET':
        payment = Payment.objects.all()
        serializer = PaymentSerializer(payment, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PaymentSerializer(data=request.data)
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
            if Token.objects.filter(id=api_key).exists():
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
                    payment = Payment(
                        phone_number=phone_number,
                        amount=amount,
                        reference=reference,
                        api_key=api_key
                    )
                    payment.save()

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
                "token": api_key

            }

            resp = requests.post(url=url, json=json_data)
            print(resp.status_code)
            print(resp.text)

            return Response(resp.text)

        else:
            return Response({'data': "token invalido"})



