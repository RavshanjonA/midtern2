from django.urls import path

from apps.task2.api_endpoints.vacancy import VacancyListAPIView

app_name = "task2"

urlpatterns = [
    path("vacancies/", VacancyListAPIView.as_view(), name="product-list"),
]
