from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.db.models.manager import BaseManager
from django.db.models.query import QuerySet
from django.utils import timezone
from multiselectfield import MultiSelectField

age_choices = (
    ('Youth', 'Youth'),
    ('Young Adult', 'Young Adult'),
    ('Adult', 'Adult'),
    ('All Ages', 'All Ages'),
)

skill_choices = (
    ('Newbie', '2 years or less'),
    ('Intermediate', '3-5 years'),
    ('Experienced', '5+'),
    ('No Skill Level', 'No Skill level')
)
tech_experience_choices = (
    ('Education', 'Education'),
    ('Social', 'Social'),
    ('Conference', 'Conference'),
    ('Special Events', 'Special Events'),
    ('Youth Programs', 'Youth Programs')
)
programming_language_choices = (
    ('Python', 'Python'),
    ('Javascript', 'Javascript'),
    ('Java', 'Java'),
    ('HTML', 'HTML'),
    ('C Programming Language', 'C Programming Language'),
    ('CSS', 'CSS'),
    ('Django', 'Django'),
    ('ReactJS', 'ReactJS'),
    ('React Native', 'React Native'),
    ('Swift', 'Swift'),
    ('SQL', 'SQL'),
    ('Ruby', 'Ruby'),
    ('Node.JS', 'Node.JS'),
    ('UI/UX', 'UI/UX')
)


# Create your models here.
# class UserManager(BaseManager):
#     def create_user(self, first_name, last_name, username, password, email, age_group, skill_level, tech_experience):
#         if not username:
#             raise ValueError('Please Enter a Username')
#         if not password:
#             raise ValueError('Please Enter a Password')
#         if not email:
#             raise ValueError('Please Enter an Email')
#         user = self.model(
#             first_name=first_name,
#             last_name=last_name,
#             username=username,
#             password=password,
#             email=email,
#             age_group=age_group,
#             skill_level=skill_level,
#             tech_experience=tech_experience
#
#         )
#         user.set_password = password
#         user.is_valid = True
#         user.save(using=self._db)
#         return user
#
#     def filter(self, status):
#         return self.filter(status=self.model.STATUS_POST_COMPLETE)


class Event(models.Model):
    event_name = models.CharField(max_length=600)
    location = models.CharField(max_length=600)
    time = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateField(default=date.today)
    organization = models.CharField(max_length=300, null=True, blank=True)
    event_image = models.ImageField(upload_to='media', null=True, blank=True)
    description = models.CharField(max_length=6000)
    event_skill_level = MultiSelectField(choices=skill_choices, null=True, blank=True)
    event_age_group = MultiSelectField(choices=age_choices, null=True, blank=True)
    programming_language = MultiSelectField(choices=programming_language_choices, null=True, blank=True)
    event_category = MultiSelectField(choices=tech_experience_choices)

    def __str__(self):
        return f"{self.event_name} {self.location} {self.event_image} {self.description} " \
               f"{self.event_age_group} {self.programming_language} {self.event_category}"


class UserChoices(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=20, default=' ')
    last_name = models.CharField(max_length=20, default=' ')
    password = models.CharField(max_length=20, default=' ')
    username = models.CharField(max_length=20, default=' ')
    email = models.EmailField(max_length=150, default=' ')
    age_group = MultiSelectField(choices=age_choices, null=True, blank=False)
    skill_level = MultiSelectField(choices=skill_choices, null=True, blank=False)
    tech_experience = MultiSelectField(choices=tech_experience_choices, null=True, blank=False)
    last_login = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    groups = models.OneToOneField('auth.Group', unique=True, on_delete=models.CASCADE)

    # objects = UserManager()


# is_anonymous = models.BooleanField(default=False)
# is_authenticated = models.BooleanField(default=False)
#
# USERNAME_FIELD = 'username'
# REQUIRED_FIELDS = ['username', 'email', 'password']


class EventSelection(models.Model):
    choice = models.ForeignKey(UserChoices, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
