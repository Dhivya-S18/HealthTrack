import json
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import HealthRecord

@login_required
def health_dashboard(request):
    data = HealthRecord.objects.values("condition").annotate(count=Count("id"))
    labels = [d["condition"] for d in data]
    counts = [d["count"] for d in data]

    return render(request, "dashboard.html", {
        "labels": json.dumps(labels),
        "counts": json.dumps(counts)
    })
from django.shortcuts import render # type: ignore

@login_required # type: ignore
def my_health_records(request):
    records = HealthRecord.objects.filter(student=request.user) # type: ignore
    return render(request, "records.html", {"records": records})

@login_required # type: ignore
def add_record(request):
    if request.method == "POST":
        condition = request.POST["condition"]
        HealthRecord.objects.create(student=request.user, condition=condition) # type: ignore
        return redirect("my_records") # type: ignore
    return render(request, "add_record.html")

from django.shortcuts import render, redirect
from .models import Doctor, Appointment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def book_appointment(request):
    doctors = Doctor.objects.all()
    if request.method == "POST":
        doctor_id = request.POST["doctor"]
        date = request.POST["date"]
        time = request.POST["time"]

        doctor = Doctor.objects.get(id=doctor_id)
        # Check slot availability
        if Appointment.objects.filter(doctor=doctor, date=date, time=time).exists():
            return render(request, "book.html", {"doctors": doctors, "error": "Slot not available!"})
        
        Appointment.objects.create(student=request.user, doctor=doctor, date=date, time=time)
        return redirect("my_appointments")
    return render(request, "book.html", {"doctors": doctors})

@login_required
def my_appointments(request):
    appts = Appointment.objects.filter(student=request.user)
    return render(request, "appointments.html", {"appointments": appts})
