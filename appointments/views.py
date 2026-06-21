from django.shortcuts import render, redirect, get_object_or_404
from .models import Appointment
from .forms import AppointmentForm

# LIST
def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, "appointments/appointment_list.html", {
        "appointments": appointments
    })

# CREATE
def appointment_create(request):
    form = AppointmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('appointment_list')
    return render(request, "appointments/appointment_form.html", {"form": form})

# UPDATE
def appointment_update(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    form = AppointmentForm(request.POST or None, instance=appointment)
    if form.is_valid():
        form.save()
        return redirect('appointment_list')
    return render(request, "appointments/appointment_form.html", {"form": form})

# DELETE
def appointment_delete(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == "POST":
        appointment.delete()
        return redirect('appointment_list')
    return render(request, "appointments/appointment_delete.html", {
        "appointment": appointment
    })