# Generated by Django 5.0 on 2024-01-07 22:39

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compass', '0002_dailyagenda_tasks_userprofile_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_id',
            field=models.UUIDField(default=uuid.UUID('009dc38f-2d50-4667-a4b8-2f1fd9d0a1ca'), primary_key=True, serialize=False, unique=True),
        ),
    ]
