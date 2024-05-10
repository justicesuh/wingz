from rest_framework.viewsets import ModelViewSet

from apps.rides.models import Ride, RideEvent
from apps.rides.serializers import RideSerializer, RideEventSerializer


class RideViewSet(ModelViewSet):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer


class RideEventViewSet(ModelViewSet):
    queryset = RideEvent.objects.all()
    serializer_class = RideEventSerializer
