from django.db import models
from .paymenttypemodel import PaymentTypeModel


class PaymentModel(models.Model):
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    year = models.ForeignKey('YearModel', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        self.name = self.amount
        self.year = self.year.name
        super(PaymentModel, self).save(*args, **kwargs)

