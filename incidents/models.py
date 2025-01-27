from django.db import models
from django.conf import settings
import random
import datetime


def generate_incident_id():
    current_year = datetime.datetime.now().year
    random_number = random.randint(10000, 99999)
    return f"RMG{random_number}{current_year}"


class Incident(models.Model):
    PRIORITY_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    )
    STATUS_CHOICES = (
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('closed', 'Closed'),
    )

    USER_TYPES = (
        ('enterprise', 'Enterprise'),
        ('government', 'Government'),
    )

    reporter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    incident_id = models.CharField(max_length=20, unique=True, default=generate_incident_id, editable=False)
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='enterprise')

    description = models.TextField()
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='low')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Incident by {self.reporter.email} - {self.description[:50]}..."
