from django.urls import path

from apps.task3.api_endpoints.product import ProductAesListAPIView

app_name = "task3"

urlpatterns = [
    path("products/", ProductAesListAPIView.as_view(), name="product-list"),
]
