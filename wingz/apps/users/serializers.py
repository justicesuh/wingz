from rest_framework import serializers

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
            'date_joined',
            'role',
            'first_name',
            'last_name',
            'phone_number'
        )