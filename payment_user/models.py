from django.db import models
from django.utils.translation import gettext_lazy as _
import datetime

from user.models import User



class Payments(models.Model):
    class Services(models.TextChoices):
        NETFLIX = 'NF', _('Netflix')
        AMAZON = 'AP', _('Amazon Prime')
        STARP = 'ST', _('Star+')
        PARAMOUNT = 'PM', _('Paramount')
    
    service = models.CharField(
                                max_length=2,
                                choices=Services.choices,
                                default=Services.NETFLIX,
                                )
    payment_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    amount = models.FloatField(default=0.0)
    expiration_date = models.DateField(default=datetime.date(2023, 1, 1))

    def __str__(self) -> str:
        return f"Recibo para {self.user.username}"

