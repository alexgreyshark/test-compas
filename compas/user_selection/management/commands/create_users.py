from django.core.management.base import BaseCommand
from django.core.files import File
from user_selection.models import (
    User,
    ROLE_CHOICES,
)
import string
import random

PICTURES = (
    'user.png',
    'crm_admin.png',
    'admin.png',
)


class Command(BaseCommand):
    help = 'Создание 3-х пользователей с указанными ролями'

    def handle(self, *args, **options):
        self.create_users()

    def create_users(self, ):
        """Создание пользователей с тремя ролями
        """
        for role_tuple, pic_name in zip(ROLE_CHOICES, PICTURES):
                user = User(
                    username=''.join(random.sample(string.ascii_letters, 10)),
                    password=''.join(random.sample(string.ascii_letters, 15)),
                    role_choice=role_tuple[0],
                )
                user.avatar.save(pic_name, File(open(f"images/{pic_name}", 'rb')))
