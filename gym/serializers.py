from rest_framework import serializers
from register.models import *


class GymSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gym
        fields = ('id', 'profile1','gym_name')


class OneGymSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gym
        fields = '__all__'