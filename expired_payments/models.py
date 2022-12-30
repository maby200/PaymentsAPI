from django.db import models

# from user.models import User
from payment_user.models import Payments

# Create your models here.


class ExpiredPayment(models.Model):
    payment = models.ForeignKey(Payments, on_delete=models.CASCADE, related_name='users')
    penalty_fee_amount = models.FloatField(default=20)

    def save(self, *args, **kwargs):
        if self.payment.payment_date > self.payment.expiration_date:
            self.payment.save()
        return super(ExpiredPayment, self).save(*args,**kwargs)

    def __str__(self) -> str:
        return f"Pago expirado de {self.payment.user}"