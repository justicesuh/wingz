from rest_framework import serializers

from apps.rides.models import Ride, RideEvent


class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = (
            'status',
            'rider',
            'driver',
            'pickup_latitude',
            'pickup_longitude',
            'dropoff_latitude',
            'dropoff_longitude',
            'pickup_time',
        )


class RideEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideEvent
        fields = (
            'ride',
            'description',
            'created_at',
        )
