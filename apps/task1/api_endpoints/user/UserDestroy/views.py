from rest_framework import status
from rest_framework.generics import DestroyAPIView
from rest_framework.response import Response

from apps.common.permissions import IsTheSameUser
from apps.task1.models import User


class UserDestroyAPIView(DestroyAPIView):
    permission_classes = [IsTheSameUser]
    queryset = User.objects.all()
    lookup_field = "phone_number"

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.soft_delete()
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


__all__ = ["UserDestroyAPIView"]
