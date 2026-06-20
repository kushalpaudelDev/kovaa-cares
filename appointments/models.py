from django.db import models

class Appointment(models.Model):
    status = models.CharField(max_length=20)
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.date} - {self.status}"