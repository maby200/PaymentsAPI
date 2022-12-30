from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Services(models.Model):
    CHOICES = [
        ('NF', 'Netflix'),
        ('AP', 'Amazon Prime Video'),
        ('SP', 'Star+'),
        ('PM', 'Paramount')
    ]

    choice_field = models.CharField(max_length=2, choices=CHOICES)