from django.template.loader import render_to_string
from django.test import TestCase, Client
from .models import *
from .views import *


class Test(TestCase):
    def setUp(self):
        order = Order.objects.create(name='mehdi', created=2021, updated=2021, paid=10000, discount=10)
        order1 = Order.objects.create(name='reza', created=2021, updated=2021, paid=5000, discount=5)

        order1.save()
        order.save()

    def testorder(self):
        result = Order.objects.all()

        self.assertIn('mehdi', result[0].user)

    def testorder2(self):
        result = Order.objects.all()

        self.assertIn('reza', result[1].user)
