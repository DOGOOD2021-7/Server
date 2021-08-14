from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(AvailableDateTime)
class AvailableDateTimeAdmin(admin.ModelAdmin):
    list_display = ('id','gym','date','time','taken')
    list_display_links = ('id','gym','date','time','taken')