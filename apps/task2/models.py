from django.db import models
from django.db.models import CharField, IntegerField

from apps.common.models import BaseModel


class Vacancy(BaseModel):
    title = CharField(max_length=128)
    salary = IntegerField()
   