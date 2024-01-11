# Generated by Django 5.0 on 2024-01-07 22:45

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compass', '0004_alter_userprofile_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailyagenda',
            name='dow',
        ),
        migrations.RemoveField(
            model_name='dailyagenda',
            name='has_deadline',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_id',
            field=models.UUIDField(default=uuid.UUID('d39258c0-4e3c-4430-bb9a-a5baccf6137f'), primary_key=True, serialize=False, unique=True),
        ),
    ]