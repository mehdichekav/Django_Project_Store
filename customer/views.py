from rest_framework import permissions
from rest_framework import generics
from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User

from customer.serializers import *


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email=cd['email'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'you logged in successfully', 'success')
                return redirect('product:home')
            else:
                messages.error(request, 'username or password is wrong', 'danger')
    else:
        form = UserLoginForm()
    return render(request, 'customer/login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, 'you logged out successfully', 'success')
    return redirect('product:home')


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['email'], cd['phone'], cd['password'])
            user.save()
            messages.success(request, 'you registred successfully', 'success')
            return redirect('product:home')
    else:
        form = UserRegistrationForm()
        return render(request, 'customer/register.html', {'form': form})



# class UserListApi(generics.ListAPIView):
#     serializer_class = UserBriefSerializers
#
#     queryset = User.objects.all()
#     permission_classes = [
#         permissions.IsAuthenticated
#     ]
#
#
# class UserDetailApi(generics.RetrieveUpdateAPIView):
#     serializer_class = UserSerializer
#     # queryset = User.objects.all()
#     permission_classes = [
#         permissions
#     ]
#
#
# class AddressListApi(generics.ListAPIView):
#     serializer_class = UserSerializer
#
#     # queryset = User.objects.all()
#     def get_queryset(self):
#         return Address.objects.filter(owner=self.request.user)
#
#     # permission_classes = [
#     #     permissions.
#     # ]
#
#
# class AddressDetailApi(generics.RetrieveUpdateAPIView):
#     serializer_class = UserSerializer
#     # queryset = User.objects.all()
#     permission_classes = [
#         permissions.IsAuthenticatedOrReadOnly
#     ]
