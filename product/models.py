from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('name'))
    slug = models.SlugField(max_length=200, unique=True, verbose_name=_('slug'))

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200, verbose_name=_('name'))
    slug = models.SlugField(max_length=200, unique=True, verbose_name=_('slug'))
    image = models.ImageField(upload_to='products/%Y/%m/%d/')
    description = models.TextField(verbose_name=_('description'))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('price'))
    available = models.BooleanField(default=True, verbose_name=_('available'))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('product:product_detail', args=[self.slug, ])
    #
