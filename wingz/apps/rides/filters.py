from django_filters import rest_framework as filters

from apps.rides.models import Ride


class RideFilter(filters.FilterSet):
    rider = filters.CharFilter(field_name='rider__email', lookup_expr='iexact')

    class Meta:
        model = Ride
        fields = ('status', 'rider')
