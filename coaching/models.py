from django.db import models
from account.models import *

class Coaching(models.Model):
    dieter = models.ForeignKey(Dieter, on_delete=models.CASCADE)
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE)

