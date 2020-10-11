from rest_framework import serializers
from .models import CommunicationScheduling

class CommunicationSchedulingSerializer(serializers.ModelSerializer):

    class Meta:

        model = CommunicationScheduling
        fields = '__all__'
