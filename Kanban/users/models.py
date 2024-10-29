from django.contrib.auth.models import AbstractUser
from django.db import models


class UserStatus(models.Model):
    status_name = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['status_name']
        verbose_name = 'Статус пользователя'
        verbose_name_plural = 'Статусы пользователей'

    def __str__(self):
        return self.status_name

class User(models.Model):
    username = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
        null=True
    )
    first_name = models.CharField(
        max_length=30,
    )
    last_name = models.CharField(
        max_length=30,
    )
    image = models.ImageField(
        upload_to='user_image',
    )

    status = models.OneToOneField('UserStatus', on_delete=models.CASCADE)

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'({self.first_name} {self.last_name})'
