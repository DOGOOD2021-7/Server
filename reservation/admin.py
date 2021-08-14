from django.contrib import admin
from .models import *

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id','state','reason','','reserved_date','phone_num','client_name','gym','dieter')
    list_display_links = ('id','state','reason','','reserved_date','phone_num','client_name','gym','dieter')
