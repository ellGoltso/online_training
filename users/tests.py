from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from materials.models import Course
from users.models import Subscription, User


class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="user_for_test", email="user_for_test@mail.ru"
        )
        self.course = Course.objects.create(
            name="Тестовый курс",
            description="тест",
            owner=self.user,
        )
        self.client.force_authenticate(user=self.user)

    def test_subscribe_unsubscribe(self):
        data = {"course_subscription": self.course.pk}
        url = reverse("users:subscribe")

        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
