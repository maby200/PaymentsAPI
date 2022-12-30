from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import ExpiredPayment
from .pagination import StandardResultsSetPagination
from .serializers import ExpiredSerializer

class ExpiredViewSet(viewsets.ModelViewSet):
    """Class that lists expired payments for V2's Users"""
    queryset = ExpiredPayment.objects.get_queryset().order_by('id')
    serializer_class = ExpiredSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsAuthenticated]

    throttle_scope = 'others'