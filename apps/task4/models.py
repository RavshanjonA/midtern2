from datetime import timedelta
import random

from django.utils import timezone
from django.db.models import Model, DateTimeField, ForeignKey, CASCADE, IntegerField

from apps.task1.models import User


class Activate(Model):
    user = ForeignKey(User,CASCADE, 'codes')
    start_date = DateTimeField(auto_now=True)
    expire_date = DateTimeField(timezone.now()+timedelta(minutes=2))
    code = IntegerField(default=random.randint(2000,5000))