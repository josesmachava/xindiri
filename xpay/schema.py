import graphene

from graphene_django.types import DjangoObjectType

from mpesa.models import Transaction
from payment.models import Payment

class PaymentType(DjangoObjectType):
    class Meta:
        model = Transaction



class Query(graphene.ObjectType):
    all_payments = graphene.List(PaymentType)
    
    def resolve_all_payments(self, args):
        return Transaction.objects.all()

 
schema = graphene.Schema(query=Query)