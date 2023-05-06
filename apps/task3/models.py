from django.db.models import CharField, DecimalField, Model


class Product(Model):
    price = DecimalField(max_digits=16, decimal_places=2)
    marja = DecimalField(max_digits=16, decimal_places=2)
    package_code = CharField(max_length=58)
