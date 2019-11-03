from django.db import models
from .costtypemodel import CostTypeModel


class CostModel(models.Model):
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=100)
    year = models.ForeignKey('YearModel', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.name = self.amount
        self.year = self.year.name
        super(CostModel, self).save(*args, **kwargs)
