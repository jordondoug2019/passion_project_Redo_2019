from django.db import models
from datetime import date
from django.contrib.auth.models import User
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
    age_group = MultiSelectField(choices=age_choices, null=True, blank=True)
    skill_level = MultiSelectField(choices=skill_choices, null=True, blank=True)
    tech_experience = MultiSelectField(choices=tech_experience_choices, null=True, blank=True)


class EventSelection(models.Model):
    choice = models.ForeignKey(UserChoices, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
