from rest_framework import serializers

from apps.rides.models import Ride, RideEvent
from apps.users.serializers import UserSerializer


class RideEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideEvent
        fields = (
            'description',
            'created_at',
        )


class RideSerializer(serializers.ModelSerializer):
    rider = UserSerializer()
    driver = UserSerializer()
    events = RideEventSerializer(source='todays_ride_events', many=True)

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
            'events',
        )
