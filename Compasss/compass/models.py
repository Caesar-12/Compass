from uuid import uuid4
from django.db import models
from django.core.validators import RegexValidator
"""Base model for the compass web app"""

phone_num_valid = RegexValidator(
    regex = r'^\+?1?\d{9,15}$',
    message = 'Enter a valid phone number'
)


class UserProfile(models.Model):
    """Defines a user"""
    # __tablename__ = 'Users'
    user_id = models.UUIDField(primary_key=True, unique=True, default=uuid4())
    first_name = models.CharField(max_length=50, default='Name', blank=False)
    last_name = models.CharField(max_length=50, default='Name')
    username = models.CharField(max_length=50)
    age = models.IntegerField(blank=False)
    email = models.EmailField()
    phone = models.CharField(max_length=14, validators=[phone_num_valid], default='nil')
    password = models.CharField(max_length=50)
    c_password = models.CharField(max_length=50)


class DailyAgenda(models.Model):
    """Defines a daily tasks"""
    # __tablename__ = 'DailyAgenda'
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    dow = models.CharField(max_length=50, default='Not applicable', blank=False)
    category = models.CharField(max_length=50, default='Others', blank=False)
    has_deadline = models.BooleanField()
    tasks = models.JSONField()
