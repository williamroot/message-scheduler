from .models import CommunicationScheduling
from .serializers import CommunicationSchedulingSerializer
from rest_framework import viewsets, mixins


class CommunicationSchedulingViewSet(
        mixins.CreateModelMixin,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.DestroyModelMixin,
        viewsets.GenericViewSet):
    queryset = CommunicationScheduling.objects.all()
    serializer_class = CommunicationSchedulingSerializer
