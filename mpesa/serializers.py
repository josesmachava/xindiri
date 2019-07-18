from rest_framework import serializers
from .models import payment

class PaymentSerializer(serializers.ModelSerializer):

    class Meta:

        model = payment
        fields = '__all__'
        extra_kwargs = {'mpesaReturn': {'required': False},
                        'transaction_id': {'required': False},
                        'transaction_status_code': {'required': False},
                        'transaction_status': {'required': False},
                        'website': {'required': False}
                        }