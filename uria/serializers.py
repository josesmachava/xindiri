from rest_framework import serializers
from .models import Transaction

class TransationSerializer(serializers.ModelSerializer):

    class Meta:

        model = Transaction
        fields = '__all__'
        extra_kwargs = {'phone_number': {'required': False},
                        'amount': {'required': False},
                        'reference': {'required': False},
                        'api_key': {'required': False},
                        }