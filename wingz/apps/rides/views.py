from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters

from apps.rides.filters import RideFilter
from apps.rides.models import Ride, RideEvent
from apps.rides.serializers import RideSerializer, RideEventSerializer


class RideViewSet(ModelViewSet):
    queryset = Ride.objects.select_related('rider').select_related('driver').prefetch_related('events').all()
    serializer_class = RideSerializer
    filterset_class = RideFilter
    ordering = ('pickup_time',)


class RideEventViewSet(ModelViewSet):
    queryset = RideEvent.objects.all()
    serializer_class = RideEventSerializer
