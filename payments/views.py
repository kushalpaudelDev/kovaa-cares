from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
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

    if appointment.payments.filter(status='Paid').exists():
        messages.info(request, 'This appointment has already been paid.')
        return redirect('payment_list')

    if appointment.status == 'Cancelled':
        messages.error(request, 'Cannot pay for a cancelled appointment.')
        return redirect('appointment_list')

    if request.method == 'POST':
        try:
            Payment.objects.create(
                appointment=appointment,
                amount=appointment.service.price,
                payment_method='manual',
                transaction_id=f"manual-{appointment.id}-{timezone.now().strftime('%Y%m%d%H%M%S')}",
                status='Paid'
            )
            messages.success(request, 'Payment successful.')
            return redirect('payment_list')
        except Exception as e:
            messages.error(request, str(e))
            return redirect('payment_page', appointment_id=appointment_id)

    return render(request, 'payments/payment_page.html', {'appointment': appointment})
