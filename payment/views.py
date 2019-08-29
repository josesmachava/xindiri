from django.shortcuts import render
import json
import requests
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PaymentSerializer


# Create your views here.
def phone_number(request):
    
    return render(request, 'payment/payment.html')




@api_view(['GET', 'POST'])
def Mpesa(request):
    """
    List all code Payment, or create a new Payment.
    """
    #Get Data from Post API
    serializer = PaymentSerializer(data=request.data)
    if serializer.is_valid():
        requestPayment = request.data
        checkToken = requestPayment[""]
        contact    = requestPayment[""]
        amount     = requestPayment[""]
        reference  = requestPayment[""]
        api_key    = requestPayment[""]
        public_key = requestPayment[""]

    


        if checkToken != "":

            
            if contact != "" and amount != "" and reference != "" and api_key != "" and public_key != "" :
                return Response({'data': "token invalido"})


 
        




















  







        
        