from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from pets.models import Pet
from appointments.models import Appointment
from payments.models import Payment
from reviews.models import Review


def home(request):
    context = {}
    if request.user.is_authenticated:
        context = {
            "pet_count": Pet.objects.filter(owner=request.user).count(),
            "appointment_count": Appointment.objects.filter(pet__owner=request.user).count(),
            "pending_appointments": Appointment.objects.filter(pet__owner=request.user, status="Pending").count(),
            "paid_payments": Payment.objects.filter(appointment__pet__owner=request.user, status="Paid").count(),
            "review_count": Review.objects.filter(user=request.user).count(),
        }
    return render(request, "home.html", context)


@login_required
def dashboard(request):

    total_pets = Pet.objects.filter(owner=request.user).count()
    total_appointments = Appointment.objects.filter(pet__owner=request.user).count()
    pending = Appointment.objects.filter(pet__owner=request.user, status="Pending").count()
    completed = Appointment.objects.filter(pet__owner=request.user, status="Completed").count()
    payments_pending = Payment.objects.filter(appointment__pet__owner=request.user).exclude(status="Paid").count()
    review_count = Review.objects.filter(user=request.user).count()

    context = {
        "total_pets": total_pets,
        "total_appointments": total_appointments,
        "pending": pending,
        "completed": completed,
        "payments_pending": payments_pending,
        "review_count": review_count,
    }

    return render(request, "dashboard.html", context)