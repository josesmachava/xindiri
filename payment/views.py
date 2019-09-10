from django.shortcuts import render
import json
import requests
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PaymentSerializer
from .models import  Payment


# Create your views here.
def phone_number(request):
    
    return render(request, 'payment/payment.html')




@api_view(['GET', 'POST'])
def Mpesa(request):
    """
    List all code Payment, or create a new Payment.
    """
    if request.method == 'GET':
        payments = Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)


    #Get Data from Post API
    elif request.method == 'POST':
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            requestPayment = request.data
            checkToken = requestPayment["token"]
            contact    = requestPayment["contact"]
            amount     = requestPayment["amount"]
            reference  = requestPayment["reference"]
            api_key    = requestPayment["api_key"]
            public_key = requestPayment["public_key"]
            website    = requestPayment["website"]
    


        if checkToken != "":

            requestCheck = ""

            if requestCheck == 0:
                return Response("Requests :Sorry you don't have it!!!", status=status.HTTP_400_BAD_REQUEST)

                if contact == "" and amount == "" and reference == "" and api_key == "" and public_key == "" :
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                


 
        




















  







        
        