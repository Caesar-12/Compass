from django.contrib import admin
from .models import BaseModel, UserProfile, DailyAgenda


# Register your models here.
admin.site.register(BaseModel)
admin.site.register(UserProfile)
admin.site.register(DailyAgenda)
