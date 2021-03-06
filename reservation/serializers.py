from rest_framework import serializers
from reservation.models import *


class ReservationGymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gym
        fields = ('id', 'logo', 'gym_name')

class GymReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ('id', 'state','gym','phone_num','reserved_date','client_name','created_at','updated_at')

    def to_representation(self, instance): #shop에서 필요한 정보만 표시
        response = super().to_representation(instance)
        response['gym'] = ReservationGymSerializer(instance.gym, context={"request": self.context['request']}).data
        return response

class DieterReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ('id', 'state','gym','phone_num','reserved_date', 'reason')

    def to_representation(self, instance): #shop에서 필요한 정보만 표시
        response = super().to_representation(instance)
        response['gym'] = ReservationGymSerializer(instance.gym, context={"request": self.context['request']}).data
        return response
