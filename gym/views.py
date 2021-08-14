from django.shortcuts import get_object_or_404
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *




class GymList(APIView):

    def get(self, request):
        gyms = Gym.objects.all()
        data = GymSerializer(gyms ,many=True, context={"request": request})

        return Response(data, status=status.HTTP_200_OK)


class GymDetail(APIView):

    def get(self,request,pk):
        gym = get_object_or_404(Gym, pk=pk)
        data = OneGymSerializer(gym, context={"request": request})

        return Response(data, status=status.HTTP_200_OK)


class ReservationTimeDetail(APIView):

    def get(self, request, pk):
        gym = get_object_or_404(Gym, pk=pk)
        date = request.query_params['date'] # requset parameter 가져오기

        times = AvailableDateTime.filter(date = date, gym=gym)
        data = AvailableDateTimeSerializer(times, many=True)

        return Response(data, status=status.HTTP_200_OK)


