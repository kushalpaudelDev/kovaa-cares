from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    RATING_CHOICES = [
        (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'),
        (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'reviews'
        ordering = ['-created_at']
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return f"{self.user.username} - {self.rating}"