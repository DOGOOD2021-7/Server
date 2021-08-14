from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id','email','type',)
    list_display_links = ('id','email','type',)

@admin.register(Dieter)
class DieterAdmin(admin.ModelAdmin):
    list_display = ('username','user','profile','address',)
    list_display_links = ('username','user','profile','address',)

@admin.register(Gym)
class GymAdmin(admin.ModelAdmin):
    list_display = ('user','gym_name','address',)
    list_display_links = ('user','gym_name','address',)