from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from register.views import get_user
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import *

# Create your views here.
class AddRecord(APIView): #기록 추가
    def post(self, request):
        user = get_user(request) #jwt에서 user읽기
        body=request.data
        Record.objects.create(dieter=user.dieter,comment=body["comment"],inbody=body["inbody"])
        return Response({"detail":"success"},status=status.HTTP_201_CREATED)

class OneRecord(APIView):
    def get(self, request,pk): #특정 기록 조회
        record = get_object_or_404(Record,pk=pk)
        serializer = RecordSerializer(record, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request,pk): #특정 기록 삭제
        record = get_object_or_404(Record,pk=pk)
        record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)