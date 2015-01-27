__author__ = 'tyan'
from django.test import TestCase
from django.contrib.auth.models import User
from .serializers import *

class UserSerializersCase(TestCase):
    def setUp(self):
        User.objects.create(username="lion", password="hi", first_name="fuck", last_name="fuck", email="hi@gmail.com")

    def test_animals_can_speak(self):
        lion = User.objects.get(username="lion")
        self.assertEqual(lion.email, 'hi@gmail.com')