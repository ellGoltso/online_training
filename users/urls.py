from users.apps import UsersConfig
from django.urls import path
from users.views import (
    PaymentCreateAPIView,
    PaymentListAPIView,
    UserCreateAPIView,
    UserUpdateAPIView,
    UserRetrieveAPIView,
    UserDestroyAPIView,
    SubscriptionAPIView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = UsersConfig.name

urlpatterns = [
    path("payment/create/", PaymentCreateAPIView.as_view(), name="payment-create"),
    path("payment/", PaymentListAPIView.as_view(), name="payment-list"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path("user/update/<int:pk>/", UserUpdateAPIView.as_view(), name="user-update"),
    path("user/<int:pk>/", UserRetrieveAPIView.as_view(), name="user"),
    path("user/delete/<int:pk>/", UserDestroyAPIView.as_view(), name="user-delete"),
    path("subscribe/", SubscriptionAPIView.as_view(), name="subscribe"),
]
