from django.db import models
from .costtypemodel import CostTypeModel


class CostModel(models.Model):
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    costtype = models.ForeignKey(CostTypeModel, on_delete=models.DO_NOTHING)
    year = models.ForeignKey('YearModel', on_delete=models.DO_NOTHING)

