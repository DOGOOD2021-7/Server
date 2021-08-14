from rest_framework import serializers
from register.models import *
from .models import *


class GymSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gym
        fields = ('id', 'profile1','gym_name','address','address_detail')


class OneGymSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gym
        fields = '__all__'

class AvailableDateTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableDateTime
        fields = ('id','time', 'date','taken')
