# Generated by Django 5.1.2 on 2024-10-30 10:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_alter_task_commit_url'),
        ('users', '0002_alter_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='employe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
    ]
