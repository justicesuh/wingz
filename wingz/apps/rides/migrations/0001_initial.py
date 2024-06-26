# Generated by Django 5.0.1 on 2024-05-10 22:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('en-route', 'En-route'), ('pickup', 'Pickup'), ('dropoff', 'Dropoff')], default='en-route', max_length=8, verbose_name='status')),
                ('pickup_latitude', models.DecimalField(decimal_places=6, max_digits=8, verbose_name='pickup latitude')),
                ('pickup_longitude', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='pickup longitude')),
                ('dropoff_latitude', models.DecimalField(decimal_places=6, max_digits=8, verbose_name='dropoff latitude')),
                ('dropoff_longitude', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='dropoff longitude')),
                ('pickup_time', models.DateTimeField(blank=True, null=True, verbose_name='pickup time')),
                ('driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='driver_rides', to=settings.AUTH_USER_MODEL)),
                ('rider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='passenger_rides', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RideEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=64, verbose_name='description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('ride', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events', to='rides.ride')),
            ],
        ),
    ]
