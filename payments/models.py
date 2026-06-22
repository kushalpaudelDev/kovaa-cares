from django.db import models
from appointments.models import Appointment
from django.db.models.signals import post_save
from django.dispatch import receiver
from notifications.models import Notification


class Payment(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Paid', 'Paid'),
        ('Failed', 'Failed'),
        ('Refunded', 'Refunded'),
    ]

    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    transaction_id = models.CharField(max_length=100, blank=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    paid_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.amount} - {self.status}"


@receiver(post_save, sender=Payment)
def payment_post_save(sender, instance, created, **kwargs):
    # If payment is marked as Paid, confirm the appointment and notify the user
    if instance.status == 'Paid':
        appointment = instance.appointment
        if appointment.status != 'Confirmed':
            appointment.status = 'Confirmed'
            appointment.save()
        # create notification for the appointment owner
        try:
            user = appointment.pet.owner
            Notification.objects.create(
                user=user,
                title='Payment Received',
                message=f'Payment of {instance.amount} received. Your appointment is confirmed.'
            )
        except Exception:
            pass