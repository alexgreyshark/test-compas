from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, User
from .managers import CustomUserManager

ROLE_CHOICES = (
    ('simple_user', 'Пользователь'),
    ('manager', 'Мененджер'),
    ('crm-admin', 'CRM-Администратор'),
)


class User(AbstractBaseUser, PermissionsMixin):
    """Модель User, замена django.contrib.auth.models.User
    """
    username = models.CharField(
        max_length=35,
        verbose_name='Никнейм',
        unique=True,
    )
    role_choice = models.CharField(
        max_length=25,
        choices=ROLE_CHOICES,
        null=True,
        verbose_name='Роль',
    )
    offer = models.BooleanField(
        verbose_name='Предложение',
        null=True,
    )
    avatar = models.ImageField(
        blank=False,
    )
    is_staff = models.BooleanField(
        default=False,
    )
    is_active = models.BooleanField(
        default=True,
    )
    is_superuser = models.BooleanField(
        default=False,
    )
    date_joined = models.DateTimeField(
        default=timezone.now,
    )

    USERNAME_FIELD = 'username'

    objects = CustomUserManager()

    def __str__(self):
        return self.username
