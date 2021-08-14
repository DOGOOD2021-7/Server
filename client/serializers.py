from rest_framework import serializers
from register.models import *
from .models import *
from record.models import *


class ClientSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField('get_profile')  # client의 profile가져오기
    
    class Meta:
        model = Coaching
        fields = ('id', 'client','client_name','profile')

    def get_profile(self, obj):  # client의 profile가져오기
        return obj.client.profile

class ClientRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Record
        fields = '__all__'

