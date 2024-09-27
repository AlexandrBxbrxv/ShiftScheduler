import os

from django.core.management import BaseCommand
from users.models import User
from dotenv import load_dotenv
from config.settings import BASE_DIR

load_dotenv(BASE_DIR / '.env')


class Command(BaseCommand):
    """Создает суперпользователя"""
    def handle(self):
        superuser = User.objects.create_user(
            email=os.getenv('ADMIN_EMAIL'),
            is_staff=True,
            is_superuser=True
        )
        superuser.superuser(os.getenv('ADMIN_PASSWORD'))
        superuser.save()

