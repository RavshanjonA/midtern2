from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.task2.models import Vacancy


@admin.register(Vacancy)
class VacancyAdmin(ModelAdmin):
    list_display = ['title', 'salary']

