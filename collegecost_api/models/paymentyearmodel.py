from django.db import models
from .yearmodel import YearModel
from .paymentmodel import PaymentModel

class PaymentYearModel (models.Model):
    payment = models.ForeignKey(PaymentModel, on_delete=models.DO_NOTHING)
    year = models.ForeignKey(YearModel, on_delete=models.DO_NOTHING)

