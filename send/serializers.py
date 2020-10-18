from rest_framework import serializers
from .models import  Payment


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:

        model = Payment
        fields = '__all__'
        extra_kwargs = {'phone_number': {'required': False},
                        'amount': {'required': False},
                        'reference': {'required': False},
                        'api_key': {'required': False},
                        }