# Generated by Django 5.0 on 2024-01-07 22:44

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compass', '0003_alter_userprofile_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_id',
            field=models.UUIDField(default=uuid.UUID('2ce7bc45-576f-4521-9423-4f9e47c6bbde'), primary_key=True, serialize=False, unique=True),
        ),
    ]
