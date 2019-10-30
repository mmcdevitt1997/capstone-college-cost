from django.db import models
from .paymenttypemodel import PaymentTypeModel


class PaymentModel(models.Model):
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    paymenttype = models.ForeignKey(PaymentTypeModel, on_delete=models.DO_NOTHING)
    year = models.ForeignKey('YearModel', on_delete=models.DO_NOTHING)