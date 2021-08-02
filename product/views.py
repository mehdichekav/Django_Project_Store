from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.utils.translation import gettext as _


def home(request):
    products = Product.objects.filter(available=True)
    return render(request, 'product/home.html', {_('products'): products})


def product_detail(request, slug):
    products = get_object_or_404(Product, slug=slug)
    return render(request, 'product/product_detail.html', {_('products'): products})
