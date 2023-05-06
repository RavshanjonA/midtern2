from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.task2.api_endpoints.vacancy.VacancyList.filters import \
    VacancySalaryFilter
from apps.task2.api_endpoints.vacancy.VacancyList.serializers import \
    VacancyListSerializer
from apps.task2.models import Vacancy


class VacancyListAPIView(ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyListSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = VacancySalaryFilter


__all__ = ["VacancyListAPIView"]
