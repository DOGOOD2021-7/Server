from django.shortcuts import get_object_or_404
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
from register.views import get_user
import json
import datetime



class GymList(APIView):

    def get(self, request):
        gyms = Gym.objects.all()
        serializer = GymSerializer(gyms ,many=True, context={"request": request})
        user = get_user(request)
        if user.type == "gym":
            user_address = user.gym.address
        else:
            user_address = user.dieter.address
        return_dict = {'user_address':user_address, 'data': serializer.data}
        return Response(return_dict, status=status.HTTP_200_OK)


class GymDetail(APIView):

    def get(self,request,pk):
        gym = get_object_or_404(Gym, pk=pk)
        serializer = OneGymSerializer(gym, context={"request": request})

        return Response(serializer.data, status=status.HTTP_200_OK)


class ReservationTimeDetail(APIView):

    def get(self, request, pk):
        gym = get_object_or_404(Gym, pk=pk)
        date = request.query_params['date'] # request parameter 가져오기
        date = datetime.datetime.strptime(date,'%Y-%m-%d') # datetime으로 만들기

        times = gym.availableTimes.filter(date = date)
        serializer = AvailableDateTimeSerializer(times, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)