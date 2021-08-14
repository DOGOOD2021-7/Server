from django.db import models
from register.models import *


class AvailableDateTime:
    Time_CHOICES = (
        (9, '9 : 00'),
        (10, '10 : 00'),
        (11, '11 : 00'),
        (12, '12 : 00'),
        (13, '13 : 00'),
        (14, '14 : 00'),
        (15, '15 : 00'),
        (16, '16 : 00'),
        (17, '17 : 00'),
        (18, '18 : 00'),
        (19, '19 : 00'),
        (20, '20 : 00'),
        (21, '21 : 00'),
    )
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.IntegerField(choices=Time_CHOICES)
