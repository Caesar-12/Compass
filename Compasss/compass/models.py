from uuid import uuid4
from django.db import models
from .base_model import BaseModel
"""Base model for the compass web app"""
# Create your models here.


class UserProfile(BaseModel):
    """Defines a user"""
    # __tablename__ = 'Users'
    user_id = models.UUIDField(primary_key=True, unique=True, default=uuid4())
    first_name = models.CharField(max_length=50, default='Name', blank=False)
    last_name = models.CharField(max_length=50, default='Name')
    userame = models.CharField(max_length=50)
    age = models.IntegerField(blank=False)
    ed_level = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    c_password = models.CharField(max_length=50)


class DailyAgenda(BaseModel):
    """Defines a daily tasks"""
    # __tablename__ = 'DailyAgenda'
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    dow = models.CharField(max_length=50, default='Not applicable', blank=False)
    category = models.CharField(max_length=50, default='Others', blank=False)
    has_deadline = models.BooleanField()
