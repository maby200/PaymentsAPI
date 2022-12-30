from . import api
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r"", api.ExpiredViewSet, "expired_payments")

urlpatterns = router.urls