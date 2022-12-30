from rest_framework import serializers

from payment_user.models import Payments
from expired_payments.models import ExpiredPayment
from services.models import Services


class PaymentsSerializerV2(serializers.ModelSerializer):
    """Serializer for expired payments in V2"""
    class Meta:
        model = Payments
        fields = '__all__'
        read_only_fields = (
                            'payment_date',
                            'user',
                            'amount'
                            )

class ExpiredSerializerV2(serializers.ModelSerializer):
    """Serializer for expired payments in V2"""
    class Meta:
        model = ExpiredPayment
        fields = '__all__'
        read_only_fields = '__all__',

# ServiceSerializer is in /services/serializers.py