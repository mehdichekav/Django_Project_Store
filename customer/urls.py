from django.urls import path, include
from django.views.generic import TemplateView

from . import views
from . import api_views
from rest_framework.authtoken.views import obtain_auth_token


app_name = 'customer'

api_urls = [
    path('user/', api_views.UserListView.as_view()),
    path('user/create/', api_views.UserCreateView.as_view()),
    path('user/update/<int:pk>/', api_views.UserUpdateView.as_view()),
    path('user/delete/<int:pk>/', api_views.UserDeleteView.as_view()),

    path('address/', api_views.AddressListView.as_view()),
    path('address/create/', api_views.AddressCreateView.as_view()),
    path('address/update/<int:pk>/', api_views.AddressUpdateView.as_view()),
    path('address/delete/<int:pk>/', api_views.AddressDeleteView.as_view()),

    path('token-auth/', obtain_auth_token),
]

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
    path('profile/', views.user_profile, name='profile'),
    path('update/', views.user_update, name='update'),
    path('change/', views.change_password, name='change'),
    path('test/', TemplateView.as_view(template_name='text.html')),
    path('api/', include(api_urls)),
    # path('user/', UserListApi.as_view(), name='user'),
    # path('user/<int:pk>', UserDetailApi.as_view(), name='user'),
    # path('Address/',AddressListApi.as_view(), name='user'),
    # path('Address/<int:pk>', AddressDetailApi.as_view(), name='user'),
    ]

