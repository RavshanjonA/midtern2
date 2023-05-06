from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.task3.models import Product


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ("price", "marja", "package_code")
