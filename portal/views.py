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

