from django.utils import timezone
from django.db import models
from datetime import date
from users.models import User


class Board(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Доска'
        verbose_name_plural = 'Доски'

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=255)
    created_at = timezone.now()
    description = models.TextField(blank=True, null=True)
    commit_url = models.CharField(max_length=255, blank=True, null=True)
    employe = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text_comment = models.TextField()
    created_at = timezone.now()

    task = models.ForeignKey(Task, related_name='comments', on_delete=models.CASCADE)

    class Meta:
        ordering = ['user']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.user.last_name} {self.user.first_name}: {self.text_comment}'
