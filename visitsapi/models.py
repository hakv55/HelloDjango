from django.db import models

# Create your models here.

class Visit(models.Model):

    user_id = models.CharField(max_length=2)
    latitude = models.DecimalField(max_digits=8, decimal_places=6)
    longitude = models.DecimalField(max_digits=8, decimal_places=6)
    rate = models.DecimalField(max_digits=8, decimal_places=2)
