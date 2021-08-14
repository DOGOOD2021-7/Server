from django.shortcuts import get_object_or_404
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *




class GymList(APIView):

    def get(self, request):
        gyms = Gym.objects.all()
        serializer = GymSerializer(gyms ,many=True, context={"request": request})

        return Response(serializer.data, status=status.HTTP_200_OK)


class GymDetail(APIView):

    def get(self,request,pk):
        gym = get_object_or_404(Gym, pk=pk)
        serializer = OneGymSerializer(gym, context={"request": request})

        return Response(serializer.data, status=status.HTTP_200_OK)


class ReservationTimeDetail(APIView):

    def get(self, request, pk):
        gym = get_object_or_404(Gym, pk=pk)
        date = request.query_params['date'] # requset parameter 가져오기

        gym.availableTimes.filter(date = date)
        times = AvailableDateTime.filter(date = date, gym=gym)
        serializer = AvailableDateTimeSerializer(times, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


