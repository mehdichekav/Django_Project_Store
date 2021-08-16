from decimal import Decimal

from django.db import models
from core.models import BaseModel
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

from product.models import Product
from django.utils.translation import gettext as _


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name=_('orders'),
                             verbose_name=_('user'), help_text=_('name is user'))
    created = models.DateField(auto_now_add=True, verbose_name=_('created'))
    updated = models.DateField(auto_now=True, verbose_name=_('updated'))
    paid = models.BooleanField(default=False, verbose_name=_('paid'))  # پرداختی
    discount = models.IntegerField(blank=True, null=True, default=None, verbose_name=_('discount'))

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.user} - str({self.id})'

    def get_total_price(self):  # مجموع کل محصولات
        total = sum(item.get_cost() for item in self.items.all())
        if self.discount:
            discount_price = Decimal(self.discount / 100) * total
            return int(total - discount_price)
        return total


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name=_('orders'),
                              help_text=_('orderes'))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items',
                                verbose_name=_('product'),
                                help_text=_('products'))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('price'),
                                help_text=_('enter your prices'))
    quantity = models.PositiveSmallIntegerField(default=1, verbose_name=_('quantity'))

    def __str__(self):
        return str(self.id)

    def get_cost(self):  # هزینه هر محصول
        return self.price * self.quantity


class Coupon(models.Model):
    code = models.CharField(max_length=30, unique=True, verbose_name=_('code'), help_text=_('enter your code'))
    valid_from = models.DateTimeField(verbose_name=_('valid_from'))  # شروع اعتبار کوپن تخفیف
    valid_to = models.DateTimeField(verbose_name=_('valid_to'))  # اتمام اعتبار کوپن تخفیف
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)],
                                   verbose_name=_('discount'))
    active = models.BooleanField(default=False, verbose_name=_('active'))

    def __str__(self):
        return self.code
