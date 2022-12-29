from . import api
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r"payments", api.PaymentViewSet, "payments")

urlpatterns = router.urls