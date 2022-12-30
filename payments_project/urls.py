from django.contrib import admin
from django.urls import path, include, re_path

from versions.v2.routers import urlpatterns as v2_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r"users/", include("user.urls")),
    path('', include("payment_user.urls")),
    path('services/', include("services.urls")),
    # path for services yet to implement, so not appearing in postman
    re_path(r"^api/v2/", include(v2_urls)),
    path(r"expired-payments/", include("expired_payments.urls")),
]
