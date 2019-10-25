from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .yearmodel import YearModel
from django.contrib.auth.models import User



class CollegeModel(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    startyear = models.DateField(null=True, blank=True)
    endyear = models.DateField(null=True, blank=True)



@receiver(post_save, sender=CollegeModel)
def create_year( self, sender,  created, **kwargs):
    # does the math for how many years the user is going to college
    # by subtracting the end date year by the start date
    year = self.endyear.strftime('%Y') - self.startyear.strftime('%Y')
    # This loop should take the number of years and  create the years with the object
    for numyear in range(year):
        if created:
            YearModel.objects.create(
                name=f"year {numyear+1}",
                year=numyear+1,
                college=sender.id
            )