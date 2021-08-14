from django.db import models
from django.contrib.auth.models import User

class Gym(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gym_name = models.CharField(max_length=100)
    address = models.TextField()
    logo = models.ImageField()
    website = models.URLField()
    profile1 = models.ImageField()
    profile2 = models.ImageField()
    profile3 = models.ImageField()






