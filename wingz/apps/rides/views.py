from datetime import timedelta

from django.db.models import Prefetch
from django.utils import timezone
from rest_framework.viewsets import ModelViewSet

from apps.rides.filters import RideFilter
from apps.rides.models import Ride, RideEvent
from apps.rides.serializers import RideSerializer, RideEventSerializer


class RideViewSet(ModelViewSet):
    queryset = Ride.objects.select_related('rider').select_related('driver').prefetch_related(
        Prefetch('events', queryset=RideEvent.objects.filter(created_at__gte=(timezone.now() - timedelta(days=1))), to_attr='todays_ride_events')
    ).all()
    serializer_class = RideSerializer
    filterset_class = RideFilter
    ordering = ('pickup_time',)


class RideEventViewSet(ModelViewSet):
    queryset = RideEvent.objects.all()
    serializer_class = RideEventSerializer
