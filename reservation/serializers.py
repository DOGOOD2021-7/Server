from rest_framework import serializers
from reservation.models import *


class ReservationGymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gym
        fields = ('id', 'logo', 'gym_name')

class GymReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ('id', 'state','gym','phone_num','reserved_date','client_name')

    def to_representation(self, instance): #shop에서 필요한 정보만 표시
        response = super().to_representation(instance)
        response['gym'] = ReservationGymSerializer(instance.shop, context={"request": self.context['request']}).data
        return response

class DietReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ('id', 'state','gym','phone_num','reserved_date', 'reason')

    def to_representation(self, instance): #shop에서 필요한 정보만 표시
        response = super().to_representation(instance)
        response['gym'] = ReservationGymSerializer(instance.shop, context={"request": self.context['request']}).data
        return response
