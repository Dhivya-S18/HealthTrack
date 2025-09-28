from django.urls import path
from . import views

urlpatterns = [
    path("book/", views.book_appointment, name="book"),        # Member 1
    path("appointments/", views.my_appointments, name="my_appointments"),  # Member 2
    path("records/", views.my_health_records, name="my_records"),          # Member 2
    path("records/add/", views.add_record, name="add_record"),             # Member 3
    #path("dashboard/", views.dashboard, name="dashboard"),                 # Example dashboard
]
