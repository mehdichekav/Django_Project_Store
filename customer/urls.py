from django.urls import path
from . import views
from .views import *

app_name = 'customer'
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
    # path('user/', UserListApi.as_view(), name='user'),
    # path('user/<int:pk>', UserDetailApi.as_view(), name='user'),
    # path('Address/',AddressListApi.as_view(), name='user'),
    # path('Address/<int:pk>', AddressDetailApi.as_view(), name='user'),
    ]

