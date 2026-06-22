from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Appointment
from .forms import AppointmentForm
from pets.models import Pet
from notifications.models import Notification

# LIST
@login_required
def appointment_list(request):
    appointments = Appointment.objects.filter(pet__owner=request.user)
    return render(request, "appointments/appointment_list.html", {
        "appointments": appointments
    })

# CREATE
@login_required
def appointment_create(request):
    form = AppointmentForm(request.POST or None)
    # limit pet choices to user's pets
    form.fields['pet'].queryset = Pet.objects.filter(owner=request.user)
    if form.is_valid():
        appointment = form.save(commit=False)
        appointment.status = 'Pending'
        appointment.save()
        Notification.objects.create(
            user=request.user,
            title='Appointment Booked',
            message='Your appointment is pending confirmation'
        )
        return redirect('appointment_list')
    return render(request, "appointments/appointment_form.html", {"form": form})

# UPDATE
@login_required
def appointment_update(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    # restrict updates to owner of the pet
    if appointment.pet.owner != request.user:
        return redirect('appointment_list')
    form = AppointmentForm(request.POST or None, instance=appointment)
    # limit pet selection as well
    form.fields['pet'].queryset = Pet.objects.filter(owner=request.user)
    if form.is_valid():
        form.save()
        return redirect('appointment_list')
    return render(request, "appointments/appointment_form.html", {"form": form})

# DELETE
@login_required
def appointment_delete(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if appointment.pet.owner != request.user:
        return redirect('appointment_list')
    if request.method == "POST":
        appointment.delete()
        return redirect('appointment_list')
    return render(request, "appointments/appointment_delete.html", {
        "appointment": appointment
    })