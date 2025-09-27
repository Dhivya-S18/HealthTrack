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
