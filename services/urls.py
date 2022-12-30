from . import api
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r"", api.ServiceViewSet,"services")

urlpatterns = router.urls