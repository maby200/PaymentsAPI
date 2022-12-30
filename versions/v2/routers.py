from . import api
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r"payments-admin", api.PaymentViewSetAdmin,basename="payments-admin")
router.register(r"expired-admin", api.ExpiredViewSetAdmin,basename="expired-admin")
router.register(r"services-admin", api.ServiceViewSetAdmin, basename="services-admin")
router.register(r"payments", api.PaymentViewSetUser,basename="payments")
router.register(r"expired", api.ExpiredViewSetUser,basename="expired")
router.register(r"services", api.ServiceViewSetUser, basename="services")

urlpatterns = router.urls