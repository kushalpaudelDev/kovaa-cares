from django.db import models
from appointments.models import Appointment
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from notifications.models import Notification


class Payment(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Paid', 'Paid'),
        ('Failed', 'Failed'),
        ('Refunded', 'Refunded'),
    ]

    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    transaction_id = models.CharField(max_length=100, blank=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    paid_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.amount} - {self.status}"

    class Meta:
        db_table = 'payments'
        ordering = ['-paid_at']
        verbose_name_plural = 'Payments'


@receiver(pre_save, sender=Payment)
def payment_pre_save(sender, instance, **kwargs):
    if instance.pk:
        previous = Payment.objects.filter(pk=instance.pk).only('status').first()
        instance._previous_status = previous.status if previous else None
    else:
        instance._previous_status = None


@receiver(post_save, sender=Payment)
def payment_post_save(sender, instance, created, **kwargs):
    if instance.status == 'Paid' and instance._previous_status != 'Paid':
        appointment = instance.appointment
        if appointment.status != 'Confirmed':
            appointment.status = 'Confirmed'
            appointment.save(update_fields=['status'])
        try:
            user = appointment.pet.owner
            Notification.objects.create(
                user=user,
                title='Payment Received',
                message=f'Payment of {instance.amount} received. Your appointment is confirmed.'
            )
        except Exception:
            pass