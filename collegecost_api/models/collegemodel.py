from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .yearmodel import YearModel


class CollegeModel(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    numberofyears = models.IntegerField()

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