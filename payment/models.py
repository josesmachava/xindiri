from datetime import timezone

from django.utils import timezone
from django.db import models


# Create your models here.

class Payment(models.Model):
    contact = models.CharField(max_length=255, null=False)
    token = models.CharField(max_length=255, null=False)
    amount = models.CharField(max_length=255, null=False)
    reference = models.CharField(max_length=255, null=False)
    api_key = models.CharField(max_length=255, null=False)
    public_key = models.TextField()
    website = models.URLField()

    def __str__(self):
        return "{} - {}  -  {}".format(self.contact, self.amount, self.reference)
