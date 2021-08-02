from django.test import TestCase
from .models import Category, Product


class CategoryTest(TestCase):

    def Set_up(self) -> None:
        self.Category1 = Category.objects.create(
            name='mobile',
            slug='mobile',
        )

    def test_slug(self):

        self.assertEqual('mobile', 'mobile')


class ProductTest(TestCase):

    def Set_up(self) -> None:
        self.product1 = Product.objects.create(
            name='mobile',
            slug='mobile',
            price=20000,
            discount=10,
            image=None,

        )

        self.product2 = Product.objects.create(
            name='labtop',
            slug='labtop',
            price=20000,
            discount=0,
            image=None,

        )

        self.product3 = Product.objects.create(
            name='TV',
            slug='TV',
            price=20000,
            discount=20,
            image=None,

        )

    def test1_final_price(self):
        self.assertEqual(self.product1.price , 18000)
