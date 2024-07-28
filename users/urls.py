from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from users.apps import UsersConfig
from users.views import (PaymentListAPIView, UserCreateAPIView,
                         UserDestroyAPIView, UserListAPIView,
                         UserRetrieveAPIView, UserUpdateAPIView)

app_name = UsersConfig.name

router = DefaultRouter()

urlpatterns = [
    path(
        "users/register/",
        UserCreateAPIView.as_view(permission_classes=(AllowAny,)),
        name="register",
    ),
    path(
        "users/login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path("users/", UserListAPIView.as_view(), name="user_list"),
    path(
        "users/token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
    path("users/<int:pk>/update/", UserUpdateAPIView.as_view(), name="user_update"),
    path("users/<int:pk>/", UserRetrieveAPIView.as_view(), name="user_get"),
    path("users/<int:pk>/delete/", UserDestroyAPIView.as_view(), name="user_delete"),
    path("users/payments/", PaymentListAPIView.as_view(), name="payment_get"),
]
