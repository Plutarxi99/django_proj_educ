from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    # Создание суперюзера из-за того, что мы переопределили создание юзера. Мы не можно создать его командой createsuperuser
    def handle(self, *args, **kwargs):

        user = User.objects.create(
            email='admin@sky.pro',
            first_name='Admin',
            last_name='Admonov',
            is_superuser=True,
            is_staff=True,
            is_active=True
        )

        user.set_password('123qwe123')
        user.save()
