from django.db import models
from register.models import *


class Reservation(models.Model):
    STATE_CHOICES = (
        ('inquiry', '예약대기'),
        ('confirmed', '예약확정'),
        ('rejection', '예약취소')
    )
    state = models.CharField(choices=STATE_CHOICES, max_length=100)
    reason = models.TextField(null=True, blank=True)
    reserved_date = models.DateTimeField()
    phone_num = models.TextField()
    client_name = models.CharField(max_length=10)
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE)
    dieter = models.ForeignKey(Dieter, on_delete=models.CASCADE)

