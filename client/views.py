from django.shortcuts import get_object_or_404
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
from register.views import get_user
import json
import datetime


class ClientList(APIView):

    def get(self, request):
        gym = get_user(request).gym
        clients = gym.coaching_set.all()
        serializer = ClientSerializer(clients ,many=True, context={"request": request})

        return Response(data = serializer.data, status=status.HTTP_200_OK)


class ClientDetail(APIView):

    def get(self, request, pk):
        client = get_object_or_404(Dieter, pi=pk)
        records = Record.objects.filter(dieter=client)
        serializer = ClientRecordSerializer(records, many=True, context={"request": request})

        return Response(data = serializer.data, status=status.HTTP_200_OK)


    def post(self, request, pk):
         body = request.data
         Record.objects.create(dieter_id=pk, inbody=body['inbody'], comment=body['comment'] )

         return Response(data={'detail': 'success'}, status=status.HTTP_201_CREATED)