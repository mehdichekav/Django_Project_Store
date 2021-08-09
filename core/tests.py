from django.test import TestCase

from core.models import TestModel


class BaseModelTest(TestCase):

    def Test1(self):
        m1 = TestModel.objects.create()
        m1.deleted = True
        m1.save()
        self.assertTrue(m1.deleted)
