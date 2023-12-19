from django.contrib import admin
from .models import BaseModel, User, DailyAgenda


# Register your models here.
admin.site.register(BaseModel)
admin.site.register(User)
admin.site.register(DailyAgenda)
