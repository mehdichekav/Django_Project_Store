from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import EmailMessage

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

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


@login_required(login_url='customer:login')
def user_profile(request):
    profile = Profile.objects.get(user_id=request.user.id)
    return render(request, 'customer/profile.html', {'profile': profile})


@login_required(login_url='customer:login')
def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if user_form and profile_form.is_valid():
            # user_form.save()
            profile_form.save()
            messages.success(request, 'update successfully', 'success')
            return redirect('customer:profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'customer/update.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password changed successfully', 'success')
            return redirect('customer:profile')
        else:
            messages.error(request, 'Wrong password', 'danger')
            return redirect('customer:change')

    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'customer/change.html', {'form': form})


def contact(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        msg = request.POST['message']
        body = subject + '\n' + email + '\n' + msg
        form = EmailMessage(
            'contact form',
            body,
            'test',
            ('m.chekave.jazireh@gmail.com',),
        )
        form.send(fail_silently=False)
    return render(request, 'customer/contact.html')
