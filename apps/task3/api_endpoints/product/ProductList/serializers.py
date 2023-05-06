from rest_framework.serializers import ModelSerializer

from apps.task3.models import Product


class ProductListSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "price",
            "marja",
            "package_code",
        )
