from django.core.management.base import BaseCommand
from users.models import Payment, User
from materials.models import Course, Lesson


class Command(BaseCommand):

    def handle(self, *args, **options):
        User.objects.all().delete()
        Course.objects.all().delete()

        user, _ = User.objects.get_or_create(email="test@user.ru")

        course, _ = Course.objects.get_or_create(
            name="Курс математики",
            description="сложение, вычитание, деление, умножение",
        )
        lesson_1, _ = Lesson.objects.get_or_create(
            name="сложение", description="урок сложения", course=course
        )
        lesson_2, _ = Lesson.objects.get_or_create(
            name="вычитание", description="урок вычитания", course=course
        )
        lesson_3, _ = Lesson.objects.get_or_create(
            name="деление", description="урок деления", course=course
        )
        lesson_4, _ = Lesson.objects.get_or_create(
            name="умножение", description="урок умножения", course=course
        )

        payments = [
            {
                "user": user,
                "payment_date": "2025-11-10",
                "payment_sum": 5000,
                "paid_course": course,
            },
            {
                "user": user,
                "payment_date": "2025-11-20",
                "payment_sum": 10000,
                "paid_lesson": lesson_3,
                "payment_method": "Безналичные",
            },
        ]

        for pay in payments:
            payments, created = Payment.objects.get_or_create(**pay)

            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully added payment: {pay['user']} - {pay['payment_sum']}"
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f"Payment already exists: {pay['user']} - {pay['payment_sum']}"
                    )
                )
