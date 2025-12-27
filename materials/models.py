from django.db import models
from django.conf import settings


class Course(models.Model):
    """Модель курса"""

    name = models.CharField(max_length=150, verbose_name="Название курса")
    image = models.ImageField(
        upload_to="online_platform/preview/courses",
        blank=True,
        null=True,
        verbose_name="Превью",
    )
    description = models.TextField(verbose_name="Описание курса")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True
    )

    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"

    def __str__(self):
        return self.name


class Lesson(models.Model):
    """Модель урока"""

    name = models.CharField(max_length=50, verbose_name="Название урока")
    description = models.TextField(verbose_name="Описание урока")
    image = models.ImageField(
        upload_to="online_platform/preview/lessons",
        blank=True,
        null=True,
        verbose_name="Превью",
    )
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, verbose_name="Курс", related_name="lessons"
    )
    link_video = models.CharField(max_length=255, blank=True, null=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True
    )

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"

    def __str__(self):
        return self.name
