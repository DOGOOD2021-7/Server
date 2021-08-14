from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('id','inbody','dieter','date','comment')
    list_display_links = ('id','inbody','dieter','date','comment')