from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from pets.models import Pet
from appointments.models import Appointment


def home(request):
    return render(request, "home.html")


@login_required
def dashboard(request):

    total_pets = Pet.objects.filter(owner=request.user).count()
    total_appointments = Appointment.objects.filter(pet__owner=request.user).count()

    pending = Appointment.objects.filter(pet__owner=request.user, status="Pending").count()
    completed = Appointment.objects.filter(pet__owner=request.user, status="Completed").count()

    context = {
        "total_pets": total_pets,
        "total_appointments": total_appointments,
        "pending": pending,
        "completed": completed,
    }

    return render(request, "dashboard.html", context)