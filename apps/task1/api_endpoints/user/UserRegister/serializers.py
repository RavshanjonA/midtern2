from rest_framework import serializers

from apps.task1.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "phone_number",
            "password",
        ]
        # exclude = ['is_staff', 'is_active', 'is_superuser', 'groups', 'last_login', 'user_permissions']
