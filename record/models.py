from django.db import models
from account.models import *

class Record(models.Model):
    weight = models.CharField(max_length=10)
    muscle_mass = models.CharField(max_length=10)
    fat_mass = models.CharField(max_length=10)
    percent_body_fat = models.CharField(max_length=10)
    bmi = models.CharField(max_length=10)
    date = models.DateField(auto_now_add=True)
    dieter = models.ForeignKey(Dieter, on_delete=models.CASCADE)




