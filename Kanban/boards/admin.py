from django.contrib import admin
from boards import models

@admin.register(models.Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',

    )


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'created_at',
        'commit_url',
        'board',
    )


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'task',
        'text_comment',
        'created_at',
    )
