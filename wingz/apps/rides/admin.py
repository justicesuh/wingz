from django.contrib import admin

from apps.rides.models import Ride, RideEvent

admin.site.register(Ride)
admin.site.register(RideEvent)
