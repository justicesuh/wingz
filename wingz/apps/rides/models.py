from django.db import models
from django.db.models import ExpressionWrapper, F
from django.db.models.functions import ASin, Cos, Power, Radians, Sin, Sqrt
from django.utils.translation import gettext_lazy as _

from apps.users.models import User


class RideQuerySet(models.QuerySet):
    RADIUS_EARTH = 3961.0

    def annotate_distance(self, latitude, longitude):
        '''
        Calculate the Haversine distance from
        given coordinates to pickup coordinates
        '''
        y1 = Radians(latitude)
        x1 = Radians(longitude)
        y2 = Radians(F('pickup_latitude'))
        x2 = Radians(F('pickup_longitude'))
        dx = x2 - x1
        dy = y2 - y1
        expr = 2 * self.RADIUS_EARTH * ASin(Sqrt(Power(Sin(dy * 0.5), 2) + Cos(y1) * Cos(y2) * Power(Sin(dx * 0.5), 2)))
        return self.annotate(distance=ExpressionWrapper(expr, output_field=models.FloatField()))


class RideManager(models.Manager):
    def get_queryset(self):
        return RideQuerySet(self.model, using=self._db)

    def annotate_distance(self, latitude, longitude):
        return self.get_queryset().annotate_distance(latitude, longitude)


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
    pickup_latitude = models.DecimalField(_('pickup latitude'), max_digits=8, decimal_places=6, null=True, blank=True)
    pickup_longitude = models.DecimalField(_('pickup longitude'), max_digits=9, decimal_places=6, null=True, blank=True)
    dropoff_latitude = models.DecimalField(_('dropoff latitude'), max_digits=8, decimal_places=6, null=True, blank=True)
    dropoff_longitude = models.DecimalField(_('dropoff longitude'), max_digits=9, decimal_places=6, null=True, blank=True)
    pickup_time = models.DateTimeField(_('pickup time'), null=True, blank=True)

    objects = RideManager()


class RideEvent(models.Model):
    ride = models.ForeignKey(Ride, related_name='events', on_delete=models.SET_NULL, null=True, blank=True)
    description = models.CharField(_('description'), max_length=64)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
