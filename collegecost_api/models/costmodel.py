from django.db import models
class CostModel(models.Model):
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=100, null=True, blank=True)
    year = models.ForeignKey('YearModel', on_delete=models.CASCADE)
