from django.urls import path, include
from . import views
from . import api_views

app_name = 'orders'

api_urls = [
    path('order/', api_views.OrderListView.as_view()),
    path('order/create/', api_views.OrderCreateView.as_view()),
    path('order/update/<int:pk>/', api_views.OrderUpdateView.as_view()),
    path('order/delete/<int:pk>/', api_views.OrderDeleteView.as_view()),

    path('orderitem/', api_views.OrderItemListView.as_view()),
    path('orderitem/create/', api_views.OrderItemCreateView.as_view()),
    path('orderitem/update/<int:pk>/', api_views.OrderItemUpdateView.as_view()),
    path('orderitem/delete/<int:pk>/', api_views.OrderItemDeleteView.as_view()),

    path('coupen/', api_views.CouponView.as_view()),

]

urlpatterns = [
    path('create/', views.order_create, name='create'),
    path('<int:order_id>/', views.detail, name='detail'),
    path('apply/<int:order_id>/', views.coupon_apply, name='coupon_apply'),
    path('api-order/', include(api_urls)),
]
