from django.test import TestCase
from .models import UserChoices, User


# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username="Tumbler",
                                 password="Tumbler1")
        UserChoices.objects.get_or_create(userOnetoOne="Tumbler", first_name="Tanya",
                                          last_name="Shorts",
                                          email="tshorts@gmail.com",
                                          age_group="Youth",
                                          skill_level="No Skill Level",
                                          tech_experience="Education")
