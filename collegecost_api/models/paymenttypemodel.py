from django.db import models


class PaymentTypeModel(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=100)
    interest = models.IntegerField(null=True, blank=True)
    terminyear = models.IntegerField(null=True, blank=True)
    extramonthly = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
