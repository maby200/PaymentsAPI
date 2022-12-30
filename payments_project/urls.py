from django.contrib import admin
from django.urls import path, include, re_path


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r"users/", include("user.urls")),
    path(r"", include("payment_user.urls")),
    # path(r"services/", include("services.urls")),
    # path for services yet to implement, so not appearing in postman
    path(r"expired-payments/", include("expired_payments.urls")),
]
