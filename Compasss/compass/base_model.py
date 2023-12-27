from django.db import models
"""Bse class for models"""


class BaseModel(models.Model):
    """Defines all basic functionalities 
    needed for the Compass web app
    """

    def __init__(self) -> None:
        self.__dict = {}


    def all(self) -> None:
        """gets all obj"""
        return self.objects.all()


    def new(self, user_det: dict):
        """Inserts data into database"""
        for k, v in user_det.items():
            setattr(self, k, v)

        self.save()


    def update(self, user_id, field, value):
        """Updates users data in the db"""
        obj_update = self.objects.get(user_id=user_id)
        eval('obj_update.{} = {}'.format(field, value))
        obj_update.save()

