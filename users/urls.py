from users.apps import UsersConfig
from django.urls import path
from users.views import PaymentCreateAPIView, PaymentListAPIView

app_name = UsersConfig.name

urlpatterns = [
    path("payment/create/", PaymentCreateAPIView.as_view(), name="payment-create"),
    path("payment/", PaymentListAPIView.as_view(), name="payment-list"),
]
