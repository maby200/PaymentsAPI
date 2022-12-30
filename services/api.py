from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import  viewsets, filters

from .models import Services
from .pagination import StandardResultsSetPagination
from .serializers import ServicesSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    """Class that lists services for v2"""
    queryset = Services.objects.get_queryset().order_by('id')
    serializer_class = ServicesSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsAuthenticated]

    # search_fields = [Services.names]
    throttle_scope = 'others'