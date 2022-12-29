from django.db import models

from user.models import User
from payment_user.models import Payments

import datetime

# Create your models here.


class ExpiredPayment(models.Model):
    payment_user_id = models.ForeignKey(User, on_delete=models.CASCADE)