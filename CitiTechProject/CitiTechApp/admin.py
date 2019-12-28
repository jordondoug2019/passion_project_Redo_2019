from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import UserChoices, Event
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Event, UserChoices


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
# class UserInline(admin.StackedInline):
#     model = UserChoices
#     can_delete = False
#     verbose_name_plural = 'user'
#
#
# # Define a new User admin
# class MyUserAdmin(BaseUserAdmin):
#     inlines = (UserInline,)
#     filter_horizontal = ['groups', 'user_permissions']


# Re-register UserAdmin
admin.site.register(UserChoices)

# Register your models here.

admin.site.register(Event)
# admin.site.register(UserChoices)
