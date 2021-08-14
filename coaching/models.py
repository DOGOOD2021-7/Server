from django.db import models
from register.models import *



class Coaching:
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE)
    client = models.ForeignKey(Dieter, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=10)