from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Payment
from appointments.models import Appointment


@login_required
def payment_list(request):
    payments = Payment.objects.filter(appointment__pet__owner=request.user)
    return render(request, 'payments/payment_list.html', {'payments': payments})


@login_required
def payment_page(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    if appointment.pet.owner != request.user:
        messages.error(request, 'Unauthorized')
        return redirect('payment_list')

    if request.method == 'POST':
        try:
            # Simulate payment processing
            payment = Payment.objects.create(
                appointment=appointment,
                amount=appointment.service.price,
                payment_method='manual',
                transaction_id='tx-manual-' + str(appointment.id),
                status='Paid'
            )
            messages.success(request, 'Payment successful')
            return redirect('payment_list')
        except Exception as e:
            messages.error(request, str(e))
            return redirect('payment_page', appointment_id=appointment_id)

    return render(request, 'payments/payment_page.html', {'appointment': appointment})
from django.shortcuts import render

# Create your views here.
