from rest_framework import serializers
from .models import ExpiredPayment

class ExpiredSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpiredPayment
        fields = '__all__'
        