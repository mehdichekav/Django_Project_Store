from django.urls import path
from . import views
from .views import  ProductlistAPiView, ProductPUTApi
from django.conf import settings
from django.conf.urls.static import static

app_name = 'product'
urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:slug>/', views.product_detail, name='product_detail'),
    path('category/<slug:slug>/', views.home, name='category filter'),
    path('product_list/', views.product_list_api),
    path('product_detail_api/<str:pk>', ProductPUTApi.as_view()),
    path('product_api/', ProductlistAPiView.as_view()),
    # path('product_/', ProductPUTApi.as_view()),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
