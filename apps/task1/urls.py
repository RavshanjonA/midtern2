from django.urls import path

from apps.task1.api_endpoints.user import (LoginAPIView, UserDestroyAPIView,
                                           UserRegisterAPIView)

app_name = "task1"

urlpatterns = [
    path("register/", UserRegisterAPIView.as_view(), name="user_register"),
    path("login/", LoginAPIView.as_view(), name="user_login"),
    path("destroy/<str:phone_number>/", UserDestroyAPIView.as_view(), name="user_delete"),
]
