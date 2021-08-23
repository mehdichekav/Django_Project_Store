from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from django.conf import settings
from core.models import BaseModel


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('name'), help_text=_('enter your name'))
    slug = models.SlugField(max_length=200, unique=True, verbose_name=_('slug'), help_text=_('slug in project'))

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product:category filter', args=[self.slug, ])


class Discount(BaseModel):
    title = models.CharField(max_length=100, verbose_name=_('title'), help_text=_('enter your tittle'))
    Deduction_from_the_price = models.IntegerField(verbose_name=_('Deduction_from_the_price'),
                                                   help_text=_('enter your Deduction_from_the_price'))  # کسر از قیمت
    Cash = models.IntegerField(verbose_name=_('Cash'),
                               help_text=_('enter your Cash'))  # نقدی
    description = models.TextField(verbose_name=_('description'), help_text=_('Additional product description'))

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Discounts'

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name=_('products'),
                                 help_text=_('category'))
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, verbose_name=_('discount'),
                                 help_text=_('discount'), blank=True, null=True)
    name = models.CharField(max_length=200, verbose_name=_('name'), help_text=_('enter your name'))
    slug = models.SlugField(max_length=200, unique=True, verbose_name=_('slug'), help_text=_('slug in project'))
    image = models.ImageField(upload_to='products/%Y/%m/%d/', help_text=_('enter your image'))
    description = models.TextField(verbose_name=_('description'), help_text=_('Additional product description'))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('price'), help_text=_('price'))

    available = models.BooleanField(default=True, verbose_name=_('available'), help_text=_('This product is available '
                                                                                           'in the store'))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product:product_detail', args=[self.slug, ])
    #
    # def final_price(self):
    #     disc = self.discount or 0
    #     discounted_price = self.price * disc // 100
    #     return self.price - discounted_price


class Gallery(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('name'))
    image = models.ImageField(upload_to='gallery/', blank=True, verbose_name=_('image'))

    def __str__(self):
        return self.name
