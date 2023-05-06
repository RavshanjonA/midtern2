from django_filters import rest_framework as filters

from apps.task2.models import Vacancy


class VacancySalaryFilter(filters.FilterSet):
    salary_from = filters.NumberFilter(field_name="salary", lookup_expr="gte")
    salary_to = filters.NumberFilter(field_name="salary", lookup_expr="lte")

    class Meta:
        model = Vacancy
        fields = ["title", "salary"]
