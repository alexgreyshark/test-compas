from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = (
            'is_staff',
            'is_active',
            'groups',
            'user_permissions',
            'date_joined',
        )

