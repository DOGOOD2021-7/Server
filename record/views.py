from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from register.views import get_user
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import *

# Create your views here.
class Record(APIView): #기록 추가
    def post(self, request):
        user = get_user(request) #jwt에서 user읽기
        body=request.data
        Record.objects.create(dieter=user.dieter,comment=body["comment"],inbody=body["inbody"])
        return Response({"detail":"success"},status=status.HTTP_201_CREATED)
    
    def get(self,request): #특정 연,월에 대해 조회
        month = request.query_params['month']
        year = request.query_params['year']
        records = Record.objects.filter(date__year=year,date__month=month)
        serializer = RecordSerializer(records, many=True,context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class OneRecord(APIView):
    def get(self, request,pk): #특정 기록 조회
        record = get_object_or_404(Record,pk=pk)
        serializer = RecordSerializer(record, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request,pk): #특정 기록 삭제
        record = get_object_or_404(Record,pk=pk)
        record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)