from django.db import models
from django.db.models import F
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField


class CollegeModel(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    startyear = models.DateField(null=True, blank=True)
    endyear = models.DateField(null=True, blank=True)
    debt = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')




    class Meta:
        ordering = (F('user.date_joined').asc(nulls_last=True),)

