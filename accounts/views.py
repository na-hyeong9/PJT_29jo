from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model, login, logout
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


def index(request):
    users = get_user_model().objects.all()
    return render(request, "accounts/index.html", {"users": users})


def signup(request):
    form = CustomUserCreationForm(request.POST or None)
    if form.is_valid():
        login(request, form.save())
        return redirect("accounts:signup")
    return render(request, "accounts/signup.html", {"form": form})


def signin(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        login(request, form.get_user())
        return redirect("accounts:signup")
    return render(request, "accounts/signin.html", {"form": form})


@login_required
def signout(request):
    logout(request)
    return redirect("accounts:signin")


def detail(request, username):
    info = get_object_or_404(get_user_model(), username=username)
    return render(request, "accounts/detail.html", {"person": info})


@login_required
def follow(request, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    if person != request.user:
        if person.followers.filter(pk=request.user.pk).exists():
            person.followers.remove(request.user)
        else:
            person.followers.add(request.user)
    return redirect("accounts:detail", person.username)
