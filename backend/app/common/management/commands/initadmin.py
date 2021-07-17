import logging

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **options):
        created = 0
        self.stdout.write("Creating superusers")
        for admin_username in settings.ADMINS:
            if not User.objects.filter(username=admin_username).exists():
                user = User.objects.create_superuser(
                    admin_username, settings.ADMIN_DEFAULT_PASSWORD
                )
                user.save()
                created += 1
                self.stdout.write(f"Created superuser {admin_username} with "
                                  f"password {settings.ADMIN_DEFAULT_PASSWORD}.")
                continue
            self.stdout.write(f"Superuser {admin_username} already exist")
        self.stdout.write(f"Created {created} superusers.")

