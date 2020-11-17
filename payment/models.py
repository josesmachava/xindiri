from datetime import timezone

from django.urls import reverse
from django.utils import timezone
from django.db import models

from django.core.validators import RegexValidator

# Create your models here.
from account.models import User


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    phone_regex = RegexValidator(regex=r'^\+?84?\d{8,8}$',
                                 message="O número de telefone deve ser digitado no formato: '849394995'. São permitidos até 13 dígitos.")
    número_de_telefone = models.CharField(validators=[phone_regex], max_length=13, blank=True,
                                          unique=False)  # validators should be a list

    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.first_name}'


class Package(models.Model):
    #  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    name = models.CharField(max_length=1000)
    price = models.IntegerField(default=0)
    description = models.TextField(max_length=1000)
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['id']

    def __str__(self):

        return str(self.name)

    def get_absolute_url(self):
        return reverse('details', args=[str(self.id)])