from django.db import models
from .yearmodel import YearModel
from .costmodel import CostModel

class CostYearModel (models.Model):
    cost = models.ForeignKey(CostModel, on_delete=models.DO_NOTHING)
    year = models.ForeignKey(YearModel, on_delete=models.DO_NOTHING)

