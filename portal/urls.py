from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path("appointments/", views.my_appointments, name="my_appointments"),
    path("records/", views.my_health_records, name="my_records"),
    ]