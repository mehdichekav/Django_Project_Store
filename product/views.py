from rest_framework import generics
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from cart.forms import CartAddForm
from .models import Product, Category, Gallery
from django.utils.translation import gettext as _
from .forms import SearchForm

from .serializers import ProductSerializer


def home(request, slug=None):
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()
    gallery = Gallery.objects.all()
    if slug:
        category = get_object_or_404(Category, slug=slug)
        products = products.filter(category=category)
    return render(request, 'product/home.html', {_('products'): products, _('categories'): categories, _('gallery'): gallery})


def product_detail(request, slug):
    products = get_object_or_404(Product, slug=slug)
    # products = Product.objects.all()
    form = CartAddForm()
    return render(request, 'product/detail.html', {_('products'): products, _('form'): form})


@csrf_exempt
@api_view(['GET', 'POST'])
def product_list_api(request):
    if request.method == 'GET':
        product = Product.objects.all()
        p = ProductSerializer(product, many=True)
        return JsonResponse({'product': p.data})

    elif request.method == 'POST':
        p = ProductSerializer(data=request.POST)
        if p.is_valid():
            p.save()
            return JsonResponse(p.data)
        else:
            return JsonResponse(p.errors)


class ProductlistAPiView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductPUTApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


def product_search(request):
    products = Product.objects.all()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if data is not None:
                products = products.filter(name__exact=data)
            return render(request, 'product/detail.html',{'products': products, 'form': form})






















