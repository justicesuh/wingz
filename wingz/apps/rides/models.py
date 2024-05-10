from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.users.models import User


class Ride(models.Model):
    EN_ROUTE = 'en-route'
    PICKUP = 'pickup'
    DROPOFF = 'dropoff'
    STATUS_CHOICES = (
        (EN_ROUTE, 'En-route'),
        (PICKUP, 'Pickup'),
        (DROPOFF, 'Dropoff'),
    )

    status = models.CharField(_('status'), max_length=8, choices=STATUS_CHOICES, default=EN_ROUTE)
    rider = models.ForeignKey(User, related_name='passenger_rides', on_delete=models.SET_NULL, null=True, blank=True)
    driver = models.ForeignKey(User, related_name='driver_rides', on_delete=models.SET_NULL, null=True, blank=True)
    pickup_latitude = models.DecimalField(_('pickup latitude'), max_digits=8, decimal_places=6)
    pickup_longitude = models.DecimalField(_('pickup longitude'), max_digits=9, decimal_places=6)
    dropoff_latitude = models.DecimalField(_('dropoff latitude'), max_digits=8, decimal_places=6)
    dropoff_longitude = models.DecimalField(_('dropoff longitude'), max_digits=9, decimal_places=6)
    pickup_time = models.DateTimeField(_('pickup time'), null=True, blank=True)


class RideEvent(models.Model):
    ride = models.ForeignKey(Ride, related_name='events', on_delete=models.SET_NULL, null=True, blank=True)
    description = models.CharField(_('description'), max_length=64)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
