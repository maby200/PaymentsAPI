from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets, filters

from .models import Payments
from .pagination import StandardResultsSetPagination
from .serializers import PaymentsSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    """List payments for V1"""
    queryset = Payments.objects.get_queryset().order_by('id')
    serializer_class = PaymentsSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsAuthenticated]

    http_method_names = ['get','post']
    search_fields = ['user__id','payment_date', 'service']
    throttle_scope = 'payments'

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user = self.request.user.id)