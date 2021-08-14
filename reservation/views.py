from django.shortcuts import get_object_or_404
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
from register.views import *
from register.models import *
from gym.models import *
import json
import datetime




class ReservationList(APIView):

    def get(self, request):
        type = request.query_params['type']
        user = get_user(request)
        if type == 'dieter':
            reservations = user.dieter.reservation_set.all().order_by('-pk')
            serializer = DieterReservationSerializer ( reservations, many=True, context={"request": request})
        else:
            reservations = user.gym.reservation_set.all().order_by('-pk')
            serializer = GymReservationSerializer ( reservations, many=True, context={"request": request})



        return Response(serializer.data, status=status.HTTP_200_OK)

class AddReservation(APIView):

    def post(self, request, pk):
        gym = get_object_or_404(Gym, pk=pk)
        if get_user(request).type == 'gym':
            msg = {"detail": "gym can not access"}
            return Response(data=msg, status=status.HTTP_400_BAD_REQUEST)

        dieter = get_user(request).dieter
        date_time = json.loads(request.body.decode('utf-8')).get('datetime')

        date = date_time.split()[0]
        time = int(date_time.split()[1][:2])

        date = datetime.datetime.strptime(date, '%Y-%m-%d')

        date_time = datetime.datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S.%f')
        client_name = json.loads(request.body.decode('utf-8')).get('client_name')
        phone_num = json.loads(request.body.decode('utf-8')).get('phone_num')


        msg = {"detail": "success"}


        availableTime = gym.availableTimes.get(time = time, date = date)
        availableTime.taken = True
        availableTime.save()

        Reservation.objects.create(gym=gym, reserved_date=date_time, client_name=client_name,phone_num=phone_num,dieter=dieter)

        return Response(data=msg, status=status.HTTP_201_CREATED)
    
class ReservationsDetail(APIView):

    def patch(self,request,pk):
        gym = get_user(request).gym
        reservation = get_object_or_404(Reservation, pk=pk)
        state = json.loads(request.body.decode('utf-8')).get('state')
        reason = json.loads(request.body.decode('utf-8')).get('reason')
        msg = {"detail" : "success"}


        if state == 'rejection':
            reservation.reason = reason

            date = reservation.reserved_date.date()
            time = reservation.reserved_date.time().hour
            time = time+9
            if time >=24:
                time - 24
            availableTime = gym.availableTimes.get(time=time, date=date)
            availableTime.taken = False
            availableTime.save()


        else:
            Coaching.objects.create(gym=gym, client= reservation.dieter, client_name=reservation.client_name )

        reservation.state =state
        reservation.save()

        return Response(data=msg, status=status.HTTP_200_OK)

