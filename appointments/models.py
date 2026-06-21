from django.db import models
from pets.models import Pet

class Appointment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="appointments")
    status = models.CharField(max_length=20)
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.pet.name} - {self.date} - {self.status}"