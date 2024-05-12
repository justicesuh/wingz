from datetime import timedelta

from django.db.models import Prefetch
from django.utils import timezone
from rest_framework.viewsets import ModelViewSet

from apps.rides.filters import RideFilter
from apps.rides.models import Ride, RideEvent
from apps.rides.serializers import RideSerializer, RideEventSerializer


class RideViewSet(ModelViewSet):
    serializer_class = RideSerializer
    filterset_class = RideFilter
    ordering = ('pickup_time',)

    def get_queryset(self):
        qs = Ride.objects.select_related('rider').select_related('driver').prefetch_related(
            Prefetch('events', queryset=RideEvent.objects.filter(created_at__gte=(timezone.now() - timedelta(days=1))), to_attr='todays_ride_events')
        )
        latitude = self.request.query_params.get('latitude', None)
        longitude = self.request.query_params.get('longitude', None)
        if latitude is None or longitude is None:
            return qs.all()

        # remove OrderingFilter backend to force queryset to order by distance
        self.filter_backends = list(filter(lambda b: b.__name__ != 'OrderingFilter', self.filter_backends))
        return qs.annotate_distance(float(latitude), float(longitude)).order_by('distance').all()


class RideEventViewSet(ModelViewSet):
    queryset = RideEvent.objects.all()
    serializer_class = RideEventSerializer
