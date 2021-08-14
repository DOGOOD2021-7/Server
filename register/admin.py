from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id','email','type',)
    list_display_links = ('id','email','type',)

@admin.register(Dieter)
class DieterAdmin(admin.ModelAdmin):
    list_display = ('id','user','profile','address',)
    list_display_links = ('id','user','profile','address',)

@admin.register(Gym)
class GymAdmin(admin.ModelAdmin):
    list_display = ('id','user','gym_name','address',)
    list_display_links = ('id','user','gym_name','address',)

@admin.register(Coaching)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('id','gym', 'client', 'client_name')
    list_display_links = ('id','gym', 'client', 'client_name')
