from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.task3.api_endpoints.product.ProductList.renderers import \
    ProductAesRenderer
from apps.task3.api_endpoints.product.ProductList.serializers import \
    ProductListSerializer
from apps.task3.models import Product


class ProductAesListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    permission_classes = [IsAuthenticated]
    renderer_classes = [
        ProductAesRenderer,
    ]


__all__ = ["ProductAesListAPIView"]
