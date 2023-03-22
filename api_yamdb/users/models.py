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
        verbose_name='users_username')
    email = models.EmailField(
        max_length=254,
        unique=True,
        verbose_name='users_email')
    role = models.CharField(
        choices=CHOICES,
        default='User')
    bio = models.TextField(
        blank=True,
        verbose_name='users_bio')
    first_name = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='users_first_name')
    last_name = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='users_last_name')
    
    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        constraints = [
            models.UniqueConstraint(
                fields=['username', 'email'], name='unique_user')
        ]
