from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import Event, UserChoices

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


class UserSignUp(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        # age = forms.MultipleChoiceField(required=True,
        #                                 widget=forms.CheckboxSelectMultiple,
        #                                 choices=age_choices)
        # skill = forms.MultipleChoiceField(required=True,
        #                                   widget=forms.CheckboxSelectMultiple,
        #                                   choices=skill_choices)
        # experience = forms.MultipleChoiceField(required=True,
        #                                        widget=forms.CheckboxSelectMultiple,
        #                                        choices=tech_experience_choices)


class UserLogin(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class UserProfile(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


class ChoiceField(ModelForm):
    class Meta:
        model = UserChoices
        fields = ['age_group', 'skill_level', 'tech_experience']
    # # model = UserChoices
    # age = forms.MultipleChoiceField(required=True,
    #                                 widget=forms.CheckboxSelectMultiple,
    #                                 choices=age_choices)
    # skill = forms.MultipleChoiceField(required=True,
    #                                   widget=forms.CheckboxSelectMultiple,
    #                                   choices=skill_choices)
    # experience = forms.MultipleChoiceField(required=True,
    #                                        widget=forms.CheckboxSelectMultiple,
    #                                        choices=tech_experience_choices)
