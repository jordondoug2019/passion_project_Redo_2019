from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import UserChoices, Event


# Register your models here.

admin.site.register(Event)
admin.site.register(UserChoices)
