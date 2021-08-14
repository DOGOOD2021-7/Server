from django.shortcuts import render
from register.models import Coaching
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
# Create your views here.

class OneCoaching(APIView):
    def delete(self, request,pk): #특정 기록 삭제
        coaching = get_object_or_404(Coaching,pk=pk)
        coaching.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)