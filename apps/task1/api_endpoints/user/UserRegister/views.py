from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response

from ....models import User
from .serializers import UserRegisterSerializer


class UserRegisterAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    parser_classes = [MultiPartParser, FormParser]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            vd = serializer.validated_data
            password = vd["password"]
            phone_number = vd["phone_number"]
            first_name = vd["first_name"]
            last_name = vd["last_name"]

            user = User.objects.create(
                phone_number=phone_number,
                first_name=first_name,
                last_name=last_name,
            )
            user.set_password(password)
            user.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


__all__ = ["UserRegisterAPIView"]
