from django.urls import path
from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig
from users.views import (
    UserCreateAPIView,
    UserListAPIView,
    UserUpdateAPIView,
    UserRetrieveAPIView,
    UserDestroyAPIView,
    PaymentListAPIView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = UsersConfig.name

router = DefaultRouter()

urlpatterns = [
    path("users/create/", UserCreateAPIView.as_view(), name="user_create"),
    path("users/", UserListAPIView.as_view(), name="user_list"),
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("users/<int:pk>/update/", UserUpdateAPIView.as_view(), name="user_update"),
    path("users/<int:pk>/", UserRetrieveAPIView.as_view(), name="user_get"),
    path("users/<int:pk>/delete/", UserDestroyAPIView.as_view(), name="user_delete"),
    path("users/payments/", PaymentListAPIView.as_view(), name="payment_get"),
]
