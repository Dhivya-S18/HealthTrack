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

