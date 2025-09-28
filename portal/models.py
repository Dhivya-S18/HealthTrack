from django.db import models

# Create your models here.
from django.db import models # type: ignore

class HealthRecord(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="health_records") # type: ignore
    condition = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.condition[:20]}"

class Prescription(models.Model):
    record = models.ForeignKey(HealthRecord, on_delete=models.CASCADE, related_name="prescriptions")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE) # type: ignore
    medicine = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.medicine} ({self.dosage})"

from django.contrib.auth.models import User

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - {self.specialization}"

class Appointment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="appointments")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="appointments")
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20, choices=[("Booked", "Booked"), ("Completed", "Completed")], default="Booked")

    def __str__(self):
        return f"{self.student.username} with {self.doctor.user.username} on {self.date} {self.time}"
