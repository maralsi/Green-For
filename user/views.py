from django.shortcuts import render, redirect
from user.forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from user.models import Profile
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def register_view(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'user/register.html', context={'form': form})
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, 'user/register.html', context={'form': form})
        image = form.cleaned_data.pop('image')
        form.cleaned_data.pop("confirm_password")
        user = User.objects.create_user(
            **form.cleaned_data,
        )
        Profile.objects.create(user=user, image=image)
        return redirect('/')


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


def profile_view(request):
    if request.method == 'GET':
        posts = request.user.posts.all()
        return render(request, 'user/profile.html', context={'user': request.user})
