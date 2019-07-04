from django.db import models

# Create your models here.
class payment(models.Model):
    # song title
    contact = models.CharField(max_length=255, null=False)
    # name of artist or group/band
    amount = models.CharField(max_length=255, null=False)
    reference = models.CharField(max_length=255, null=False)
    api_key = models.CharField(max_length=255, null=False)
    public_key = models.TextField()
    mpesaReturn = models.TextField()

    def __str__(self):
        return "{} - {}  -  {}".format(self.contact, self.amount, self.reference)