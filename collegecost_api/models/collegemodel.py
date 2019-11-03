from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .yearmodel import YearModel
from .paymentmodel import PaymentModel
from .costmodel import CostModel

class CollegeModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)
    numberofyears = models.IntegerField()

    @property
    def college_total_payment(self):
        total_years = YearModel.objects.filter(college=self)
        total_payment = 0
        for x in total_years:
            payment_amount = PaymentModel.objects.filter(year=x.id)
            for payment in payment_amount:
                total_payment += payment.amount
        return total_payment

    @property
    def college_total_cost(self):
        total_years = YearModel.objects.filter(college=self)
        total_cost = 0
        for x in total_years:
            cost_amount = CostModel.objects.filter(year=x.id)
            for cost in cost_amount:
                total_cost += cost.amount
        return total_cost

    @property
    def college_balance(self):
        return  self.college_total_payment - self.college_total_cost


@receiver(post_save, sender=CollegeModel)
def create_year(instance, created, **kwargs):
    # does the math for how many years the user is going to college
    # by subtracting the end date year by the start date
    years = instance.numberofyears

    # This loop should take the number of years and  create the years with the object
    if created:
        for numyear in range(0, years):
            YearModel.objects.create(
                name=f'year {numyear+1}',
                year=numyear+1,
                college=instance
            )




