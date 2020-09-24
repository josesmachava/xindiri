from django.db import models


# Create your models here.
class Transaction(models.Model):
    phone_number = models.CharField(max_length=255, null=False)
    amount = models.CharField(max_length=255, null=False)
    reference = models.CharField(max_length=255, null=False)
    api_key = models.CharField(max_length=32, null=False)
    public_key = models.CharField(max_length=100, null=False)

    def __str__(self):
        return "{} - {}  -  {}".format(self.contact, self.amount, self.reference)
