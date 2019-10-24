from django.db import models
from djmoney.models.fields import MoneyField
from .costtypemodel import CostTypeModel


class CostModel(models.Model):
    amount = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    costtype = models.ForeignKey(CostTypeModel, on_delete=models.DO_NOTHING)