from django.db import models


class YearModel (models.Model):
    name = models.CharField(max_length=50, blank=True)
    year = models.DateField(null=True, blank=True)
    college = models.ForeignKey("CollegeModel", on_delete=models.DO_NOTHING)

