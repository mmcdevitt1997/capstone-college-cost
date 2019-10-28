from django.db import models
from .costmodel import CostModel
from .paymentmodel import PaymentModel
from .collegemodel import CollegeModel

class YearModel (models.Model):
    name = models.CharField(max_length=50, blank=True)
    year = models.DateField(null=True, blank=True)
    college = models.ForeignKey(CollegeModel, on_delete=models.DO_NOTHING)
    cost = models.ForeignKey(CostModel, on_delete=models.CASCADE )
    payment = models.ForeignKey(PaymentModel, on_delete=models.CASCADE)

@property
def yearly_cost(self):
    cost_amount = CostModel.objects.filter(year=self)
    total_cost = 0
    for cost in cost_amount:
        total_cost += cost.amount
    return total_cost

@property
def yearly_payment(self):
    payment_amount = PaymentModel.objects.filter(year=self)
    total_payment = 0
    for payment in payment_amount:
        total_payment += payment.amount
    return total_payment

