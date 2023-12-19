from uuid import uuid4
from django.db import models

"""Base model for the compass web app"""
# Create your models here.


class BaseModel(models.Model):
    """Defines all basic functionalities 
    needed for the Compass web app
    """

    def __init__(self) -> None:
        self.__dict = {}


    def create_user(self, user_dict) -> None:
        """creates a user"""
        pass

    def get_user(self, user_id) -> None:
        pass

class User(BaseModel):
    """Defines a user"""
    user_id = models.UUIDField(primary_key=True, unique=True, default=uuid4())
    first_name = models.CharField(max_length=50, default='Name', blank=False)
    last_name = models.CharField(max_length=50, default='Name')
    user_name = models.CharField(max_length=50)
    user_age = models.IntegerField(blank=False)
    user_ed_level = models.CharField(max_length=50)
    user_email = models.EmailField()
    user_password = models.CharField(max_length=50)


class DailyAgenda(BaseModel):
    """Defines a daily tasks"""
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    dow = models.CharField(max_length=50, default='Not applicable', blank=False)
    category = models.CharField(max_length=50, default='Others', blank=False)
    has_deadline = models.BooleanField()
