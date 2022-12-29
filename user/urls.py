from rest_framework import routers 

# from .routers import CustomRouter
# # necesito definir rutas.. pero no entiendo así que mejor
# # estudiar más acerca de eso

from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from . import views

# defining routers
router = routers.DefaultRouter()
# user_router = CustomRouter()


#router registration zone
router.register("", views.GetUsersView)
# user_router.register("custom/users", User)

urlpatterns = [
                path(r"signup/", views.SignupView.as_view(),name="signup"),
                path(r"login/",views.LoginView.as_view(),name="login"),
                path(r"jwt/create/", TokenObtainPairView.as_view(),name="jwt_create"),
                path(r"jwt/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
                path(r"jwt/verify/", TokenVerifyView.as_view(), name="token_verify"),
            ]

urlpatterns += router.urls