from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters

from apps.rides.filters import RideFilter
from apps.rides.models import Ride, RideEvent
from apps.rides.serializers import RideSerializer, RideEventSerializer


class RideViewSet(ModelViewSet):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = RideFilter


class RideEventViewSet(ModelViewSet):
    queryset = RideEvent.objects.all()
    serializer_class = RideEventSerializer
