from django.db import models
from django.contrib.auth.models import User


class Pet(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pets')

    SPECIES_CHOICES = [
        ('Dog', 'Dog'),
        ('Cat', 'Cat'),
        ('Bird', 'Bird'),
        ('Rabbit', 'Rabbit'),
        ('Reptile', 'Reptile'),
        ('Fish', 'Fish'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50, choices=SPECIES_CHOICES)
    breed = models.CharField(max_length=100, blank=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    vaccinated = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'pets'
        ordering = ['-created_at']
        verbose_name_plural = 'Pets'