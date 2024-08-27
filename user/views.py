from django.shortcuts import render, redirect
from user.forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def register_view(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'user/register.html', context={'form': form})
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if not form.is_valid():
            return render(request, 'user/register.html', context={'form': form})
    try:
        User.objects.create_user(
            username=form.cleaned_data['username'],
            email=form.cleaned_data['email'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            password=form.cleaned_data['password'],
        )
        User.save()
        return redirect("/")
    except IntegrityError:
        form.add_error('username', 'User or email exists')
        return render(request, 'user/register.html', context={'form': form})


def login_view(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'user/login.html', context={'form': form})
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render(request, 'user/login.html', context={'form': form})
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        if not user:
            form.add_error('username', 'User or password is incorrect')
            return render(request, 'user/login.html', context={'form': form})
        login(request, user)
        return redirect("/")


def logout_view(request):
    logout(request)
    return redirect("/")
