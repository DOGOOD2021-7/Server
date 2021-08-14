from rest_framework import serializers
from register.models import *
from .models import *
from record.models import *


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coaching
        fields = ('id', 'client','client_name' )

class ClientRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Record
        field = '__all__'

