from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название курса")
    image = models.ImageField(
        upload_to="online_platform/preview/courses",
        blank=True,
        null=True,
        verbose_name="Превью",
    )
    description = models.TextField(verbose_name="Описание курса")

    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"

    def __str__(self):
        return self.name


class Lesson(models.Model):
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

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"

    def __str__(self):
        return self.name
