from django.db import models
from django.utils import timezone

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'services'
        ordering = ['name']
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.name