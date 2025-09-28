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

