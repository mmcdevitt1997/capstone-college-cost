from django.db import models
class PaymentModel(models.Model):
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    year = models.ForeignKey('YearModel', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=100, null=True, blank=True)