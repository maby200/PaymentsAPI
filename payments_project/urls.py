from django.contrib import admin
from django.urls import path, include, re_path

from versions.v2.routers import urlpatterns as v2_urls

# Documentation
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r"users/", include("user.urls")),
    path('api/v1/', include("payment_user.urls")),
    path('api/v1/services', include("services.urls")),
    # path for services yet to implement, so not appearing in postman
    re_path(r"^api/v2/", include(v2_urls)),
    path(r"expired-payments/", include("expired_payments.urls")),


    # DRF spectacular
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
