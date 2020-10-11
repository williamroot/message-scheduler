from rest_framework import serializers
from .models import CommunicationScheduling
from django.utils import timezone


class CommunicationSchedulingSerializer(serializers.ModelSerializer):
    def validate_scheduling(self, value):
        if value < timezone.now():
            raise serializers.ValidationError(
                'O agendamento precisa ser feito em uma data futura'
            )
        return value

    class Meta:
        model = CommunicationScheduling
        fields = '__all__'
        read_only_fields = ('id', 'status')
