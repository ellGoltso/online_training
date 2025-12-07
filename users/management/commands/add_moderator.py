from django.core.management import BaseCommand
from users.models import User
from django.contrib.auth.models import Group


class Command(BaseCommand):

    def handle(self, *args, **options):
        moder, created = User.objects.get_or_create(
            username="moder", email="moder@mail.ru"
        )
        moder.set_password("1234qwer")

        if created:
            print("Модератор создан.")
        else:
            print("Модератор уже существует.")

        moderators_group = Group.objects.get(name="Moderators")

        moder.groups.add(moderators_group)
        moder.save()

        user, _ = User.objects.get_or_create(
            username="test_user_2", email="test_2@mail.ru"
        )
        user.set_password("1234qwer")
        user.save()
