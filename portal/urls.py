from django.urls import path
from . import views

urlpatterns = [
    # Member 1: Can book appointments
    path("book/", views.book_appointment, name="book"),
   
    # Member 2: Can view appointments and health records
    path("appointments/", views.my_appointments, name="my_appointments"),
    path("records/", views.my_health_records, name="my_records"),
   
    # Member 3: Can add new health records
    path("records/add/", views.add_record, name="add_record"),
   
    # Dashboard: Shared or can be member-specific
    path("dashboard/", views.health_dashboard, name="dashboard"),
]
