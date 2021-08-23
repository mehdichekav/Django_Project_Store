from django.urls import path, include
from . import views
from .views import  ProductlistAPiView, ProductPUTApi
from django.conf import settings
from django.conf.urls.static import static
from . import api_views

app_name = 'product'

api_urls = [
    path('product/', api_views.ProductListView.as_view()),
    path('product/create/', api_views.ProductCreateView.as_view()),
    path('product/update/<int:pk>/', api_views.ProductUpdateView.as_view()),
    path('product/delete/<int:pk>/', api_views.ProductDeleteView.as_view()),

    path('category/', api_views.CategoryListView.as_view()),
    path('category/create/', api_views.CategoryCreateView.as_view()),
    path('category/update/<int:pk>/', api_views.CategoryUpdateView.as_view()),
    path('category/delete/<int:pk>/', api_views.CategoryDeleteView.as_view()),

]

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:slug>/', views.product_detail, name='product_detail'),
    path('category/<slug:slug>/', views.home, name='category filter'),
    path('product_list/', views.product_list_api),
    path('product_detail_api/<str:pk>', ProductPUTApi.as_view()),
    path('search/', views.product_search, name='product_search'),
    path('product-api/', include(api_urls)),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
