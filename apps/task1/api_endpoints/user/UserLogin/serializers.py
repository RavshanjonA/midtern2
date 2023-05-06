from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    login = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)
