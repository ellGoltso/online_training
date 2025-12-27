from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from materials.models import Lesson, Course
from users.models import User


class LessonsTestCase(APITestCase):
    """Класс тестирования CRUD-операций с уроком"""

    def setUp(self):
        self.user = User.objects.create(
            username="user_for_test", email="user_for_test@mail.ru"
        )
        self.course = Course.objects.create(
            name="Тестовый курс",
            description="тест",
            owner=self.user,
        )
        self.lesson = Lesson.objects.create(
            name="test_lesson", description="урок", course=self.course, owner=self.user
        )
        self.client.force_authenticate(user=self.user)

    def test_lesson_create(self):
        data = {
            "name": "Test_lesson_",
            "description": "Test",
            "course": self.course.pk,
            "link_video": "youtube.com/test_url",
        }

        url = reverse("materials:lesson-create")
        response = self.client.post(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_lesson_update(self):
        url = reverse("materials:lesson-update", args=(self.lesson.pk,))
        data = {"name": "Test update lesson"}
        response = self.client.patch(url, data)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(data.get("name"), "Test update lesson")

    def test_lesson_retrieve(self):
        url = reverse("materials:lesson-get", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.lesson.name)

    def test_lessons_list(self):
        url = reverse("materials:lesson-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_lesson_delete(self):
        url = reverse("materials:lesson-delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)
