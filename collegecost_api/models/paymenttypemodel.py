from django.db import models
from djmoney.models.fields import MoneyField

class PaymentTypeModel(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=100)
    interest = models.IntegerField(null=True, blank=True)
    terminyear = models.IntegerField(null=True, blank=True)
    extramonthly = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', null=True, blank=True)
