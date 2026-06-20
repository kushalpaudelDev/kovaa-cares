from django.shortcuts import render
from pets.models import Pet
from appointments.models import Appointment

def home(request):
    return render(request, "home.html")


def dashboard(request):
    total_pets = Pet.objects.count()
    total_appointments = Appointment.objects.count()
    pending = Appointment.objects.filter(status="pending").count()
    completed = Appointment.objects.filter(status="completed").count()

    context = {
        "total_pets": total_pets,
        "total_appointments": total_appointments,
        "pending": pending,
        "completed": completed,
    }

    return render(request, "dashboard.html", context)