from django.contrib import admin

from users import models


@admin.register(models.UserStatus)
class UserStatusAdmin(admin.ModelAdmin):
    list_display = (
        'status_name',
        'description',
    )

@admin.register(models.User)
class User(admin.ModelAdmin):
    list_display = (
        'username',
        'first_name',
        'last_name',
        'image',
        'status',

    )