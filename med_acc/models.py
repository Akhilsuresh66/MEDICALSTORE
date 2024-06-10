from django.db import models

class Medicine(models.Model):
    id=models.DecimalField
    name = models.CharField(max_length=500)
    stock = models.DecimalField(max_digits=10, decimal_places=2)