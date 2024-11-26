from django.contrib.auth.models import AbstractUser
from django.db import models

class Alert(models.Model):
    type = models.CharField(max_length=100)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type

class DisasterAlert(models.Model):
    type = models.CharField(max_length=100)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type
        
class UserProfile(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"User Profile for {self.username}"

class DisasterAlert(models.Model):
    TYPE_CHOICES = [
        ('flood', 'Flood'),
        ('earthquake', 'Earthquake'),
        ('storm', 'Storm'),
        ('wildfire', 'Wildfire'),
    ]
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)  # Ce champ ne doit pas accepter NULL
    location = models.CharField(max_length=255)
    severity = models.IntegerField()
    description = models.TextField(null=True, blank=True)  # Facultatif
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type} at {self.location} (Severity: {self.severity})"
