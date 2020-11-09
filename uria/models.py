from django.db import models
from xpay import settings


# Create your models here.
class UriaTransaction(models.Model):
    phone_number = models.CharField(max_length=255, null=False)
    amount = models.CharField(max_length=255, null=False)
    reference = models.CharField(max_length=255, null=False)
    api_key = models.CharField(max_length=32, null=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}  -  {}".format(self.phone_number, self.amount, self.reference)
