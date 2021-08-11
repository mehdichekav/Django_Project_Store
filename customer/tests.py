from django.template.loader import render_to_string
from django.test import TestCase, Client
from .models import *
from .views import *


class Test(TestCase):
    def setUp(self):
        order = User.objects.create(name='mehdi', created=2021, updated=2021, paid=10000, discount=10)
        order1 = User.objects.create(name='reza', created=2021, updated=2021, paid=5000, discount=5)

        order1.save()
        order.save()

    def testuser(self):
        result = User.objects.all()

        self.assertIn('mehdi', result[0].user)

    def testuser2(self):
        result = User.objects.all()

        self.assertIn('mehdi', result[1].user)

