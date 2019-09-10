import json
from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Transaction
from .serializers import TransationSerializer
from account.models import Token, User
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
        transactions = Transaction.objects.all()
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
            phone_number = str(258) + str(request_transaction["phone_number"])
            # try:
            #   phone_number = str(258) + str(request_transaction["phone_number"])
            # except:
            #   return Response({"o numero de telefone e necesaria"})

            # try:
            # amount = request_transaction["amount"]
            # except:
            #   return Response({"o amout  e necesaria"})

            # try:
            # api_key = request_transaction["api_key"]
            # except:
            #  return Response({"api key e necesaria"})

            # if api_key == "":
            #   return Response("api nao pode ser vazia")

            if Token.objects.filter(id=api_key).exists():
                user = User.objects.get(token=api_key)
                print(user.email)
                if not user.is_active and not user.is_business:
                    return Response("conta nao activa e dados  nao prenchidos")
                elif not user.is_business:
                    return Response("os dados da conta nao prenchidos")
                elif not user.is_active:
                    return Response("conta nao activa")


                else:
                    transaction = Transaction(
                        phone_number=phone_number,
                        amount=amount,
                        reference=secrets.token_hex(6),
                        api_key=api_key
                    )
                    transaction.save()

            else:
                return Response("api key usado nao existe")
            return Response("salvao")

        else:
            return Response({'data': "token invalido"})