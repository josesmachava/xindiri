from django.utils import timezone

from django.db import models

# Create your models here.
class User(models.Model):
    phone_number = models.CharField(max_length=255, null=False)
    username = models.CharField(max_length=255, null=False)
    email  = models.TextField()
    website = models.URLField()
    balance = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return "{} - {}  -  {}".format(self.phone_number, self.username, self.email)