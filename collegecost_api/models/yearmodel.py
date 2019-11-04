from django.db import models
from .costmodel import CostModel
from .paymentmodel import PaymentModel



class YearModel (models.Model):
    name = models.CharField(max_length=50, blank=True)
    year = models.IntegerField()
    college = models.ForeignKey("CollegeModel", on_delete=models.CASCADE)


    class Meta:
        verbose_name = ("year")
        verbose_name_plural = ("years")
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
    @property
    def yearly_balance(self):
       return  self.yearly_payment - self.yearly_cost

