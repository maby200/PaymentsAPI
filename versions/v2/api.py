from payment_user.models import Payments
from expired_payments.models import ExpiredPayment
from services.models import Services
from .pagination import StandardResultsSetPagination
from .serializers import (PaymentsSerializerV2, ExpiredSerializerV2)
from services.serializers import ServicesSerializer

from rest_framework import viewsets, filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated

class PaymentViewSetAdmin(viewsets.ModelViewSet):
    """V2: Class based View for admin"""

    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializerV2
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAdminUser]
    
    filter_backends = [filters.SearchFilter]
    search_fields = ['payment_date','expiration_date']

    # Defining GET & POST
    def perform_create(self, serializer):
        return serializer.save(user = self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user = self.request.user.id)

class PaymentViewSetUser(viewsets.ModelViewSet):
    """ V2: Class based View for User"""

    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializerV2
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticated]
    
    filter_backends = [filters.SearchFilter]
    search_fields = ['payment_date','expiration_date']
    http_method_names = ['get','post']
    throttle_scope = 'payments'

    # Defining GET & POST
    def perform_create(self, serializer):
        return serializer.save(user = self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user = self.request.user.id)

class ExpiredViewSetAdmin(viewsets.ModelViewSet):
    """V2: Expired payments' class based view for ADMINS"""

    queryset = ExpiredPayment.objects.all()
    serializer_class = ExpiredSerializerV2
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAdminUser]

class ExpiredViewSetUser(viewsets.ModelViewSet):
    """V2: Expired payments' class based view for USERS"""

    queryset = ExpiredPayment.objects.all()
    serializer_class = ExpiredSerializerV2
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticated]
    http_method_names = ['get'] # the project says get & post but it doesnt make sense..
    throttle_scope = 'others'

class ServiceViewSetAdmin(viewsets.ModelViewSet):
    """V2: ADMIN class based view for services"""
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAdminUser]

class ServiceViewSetUser(viewsets.ModelViewSet):
    """V2: USER class based view for services"""
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticated]
    http_method_names = ['get']
    throttle_scope = 'others'

