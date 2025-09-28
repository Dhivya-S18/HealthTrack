from django.contrib import admin
from .models import Doctor, Appointment, HealthRecord, Prescription

# Register models so they appear in Django Admin
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(HealthRecord)
admin.site.register(Prescription)

# Register your models here.
