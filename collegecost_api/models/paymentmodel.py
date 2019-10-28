from django.db import models
from djmoney.models.fields import MoneyField
from .paymenttypemodel import PaymentTypeModel


class PaymentModel(models.Model):
    amount = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    paymenttype = models.ForeignKey(PaymentTypeModel, on_delete=models.DO_NOTHING)