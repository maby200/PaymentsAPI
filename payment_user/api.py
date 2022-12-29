from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, filters

from .models import Payments
from .pagination import StandardResultsSetPagination
from .serializers import PaymentsSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payments.objects.get_queryset().order_by('id')
    serializer_class = PaymentsSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsAuthenticated]

    search_fields = ['user__id','payment_date', 'service']
    throttle_scope = 'payments'