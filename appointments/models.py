from django.db import models
from pets.models import Pet
from services.models import Service


class Appointment(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='appointments')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='appointments')

    appointment_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pet.name} - {self.service}"

    @property
    def is_paid(self):
        return self.payments.filter(status='Paid').exists()

    class Meta:
        db_table = 'appointments'
        ordering = ['-appointment_date', '-created_at']
        verbose_name_plural = 'Appointments'