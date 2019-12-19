from django.contrib import admin
from .models import UserChoices, Event, User

# Register your models here.
admin.site.register(Event)
admin.site.register(UserChoices)
