from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Lesson, Course


class User(AbstractUser):
    username = models.CharField(unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

    def __str__(self):
        return self.email


class Payment(models.Model):
    CASH = "Наличные"
    NON_CASH = "Безналичные"

    METHODS_PAYMENTS = [
        (CASH, "Наличные"),
        (NON_CASH, "Безналичные"),
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="пользователь"
    )
    payment_date = models.DateField(verbose_name="дата платежа")
    paid_course = models.ForeignKey(
        Course, on_delete=models.CASCADE, blank=True, null=True
    )
    paid_lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, blank=True, null=True
    )
    payment_sum = models.PositiveSmallIntegerField(verbose_name="сумма платежа")
    payment_method = models.CharField(
        choices=METHODS_PAYMENTS, verbose_name="способ оплаты", default=CASH
    )

    def __str__(self):
        return f"{self.user} - {self.payment_method}"

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"


class Subscription(models.Model):
    user_subscription = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="пользователь"
    )

    course_subscription = models.ForeignKey(
        Course, on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return f"{self.user_subscription} - {self.course_subscription}"

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
