from django.utils import timezone

from django.db import models

# Create your models here.
class payment(models.Model):
    contact = models.CharField(max_length=255, null=False)
    phone_number = models.CharField(max_length=255, null=False)
    amount = models.CharField(max_length=255, null=False)
    reference = models.CharField(max_length=255, null=False)
    api_key = models.CharField(max_length=255, null=False)
    public_key = models.TextField()
    transaction_id = models.CharField(max_length=255, null=False)
    transaction_status_code = models.CharField(max_length=255, null=False)
    transaction_status = models.CharField(max_length=255, null=False)
    website = models.URLField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return "{} - {}  -  {}".format(self.contact, self.amount, self.reference)