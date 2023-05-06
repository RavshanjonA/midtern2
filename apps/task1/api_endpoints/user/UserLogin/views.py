from django.contrib.auth import authenticate, login
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.parsers import FormParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.common.permissions import IsTheSameUser

from .serializers import LoginSerializer


class LoginAPIView(ObtainAuthToken):
    permission_classes = [AllowAny, IsTheSameUser]
    parser_classes = [FormParser]

    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            vd = serializer.validated_data
            user = authenticate(request, username=vd["login"], password=vd["password"])
            if user:
                if not user.is_deleted:
                    login(request, user)
                    token = Token.objects.get_or_create(user=user)
                    return Response({"token": token.key}, status=status.HTTP_200_OK)
                else:
                    return Response({"status": "User not Found"}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_400_BAD_REQUEST)


__all__ = ["LoginAPIView"]
