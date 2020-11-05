from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):

    class Meta:

        model = Transaction
        fields = '__all__'
        extra_kwargs = {'phone_number': {'required': False},
                        'mpesaReturn': {'required': False},
                        'transaction_id': {'required': False},
                        'transaction_status_code': {'required': False},
                        'transaction_status': {'required': False},
                        'website': {'required': False},
                        'api_key': {'required': False},
                        'public_key': {'required': False},
                        'token':{'required': False},
                        'reference': {'required': False}
                        }