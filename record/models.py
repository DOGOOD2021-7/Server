from django.db import models
from register.models import *

class Record(models.Model):
    inbody = models.TextField() #이미지
    date = models.DateField(auto_now_add=True)
    dieter = models.ForeignKey(Dieter, on_delete=models.CASCADE)
    comment = models.TextField()



