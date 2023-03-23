from django.contrib.auth.models import AbstractUser
from django.db import models

CHOICES = (
    ('User', 'Пользователь'),
    ('Admin', 'Админ'),
    ('Moderator', 'Модератор'),
)


class CustomUser(AbstractUser):
    username = models.CharField(
        max_length=150,
        verbose_name='Ник')
    email = models.EmailField(
        max_length=254,
        unique=True,
        verbose_name='Почта')
    role = models.CharField(
        choices=CHOICES,
        default='User')
    bio = models.TextField(
        blank=True,
        verbose_name='Дополнительная информация')
    first_name = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Имя')
    last_name = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Фамилия')

    def __str__(self):
        return self.username

    def is_user(self):
        return self.role == 'User'

    def is_moderator(self):
        return self.role == 'Moderator'

    def is_admin(self):
        return self.role == 'Admin'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        constraints = [
            models.UniqueConstraint(
                fields=['username', 'email'], name='unique_user')
        ]
