from django.shortcuts import get_object_or_404
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
from register.views import *
import json
import datetime




class ReservationList(APIView):

    def get(self, request):
        type = request.query_params['type']
        user = get_user(request)
        if type == 'dieter':
            reservations = user.dieter.reservation_set.all()
            serializer = DieterReservationSerializer ( reservations, many=True, context={"request": request})
        else:
            reservations = user.gym.reservation_set.all()
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
        date_time = datetime.datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S.%f')
        client_name = json.loads(request.body.decode('utf-8')).get('client_name')
        phone_num = json.loads(request.body.decode('utf-8')).get('phone_num')
        msg = {"detail": "success"}

        Reservation.objects.create(gym=gym, reserved_date=date_time, client_name=client_name,phone_num=phone_num,dieter=dieter)

        return Response(data=msg, status=status.HTTP_201_CREATED)
    
class ReservationsDetail(APIView):

    def patch(self,request,pk):
        reservation = get_object_or_404(Reservation, pk=pk)
        state = reservation.state = json.loads(request.body.decode('utf-8')).get('state')
        reason = reservation.state = json.loads(request.body.decode('utf-8')).get('reason')
        msg = {"detail" : "success"}

        if state == 'rejection':
            reservation.reason = reason
        reservation.state =state
        reservation.save()

        return Response(data=msg, status=status.HTTP_200_OK)

