from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model, login, logout
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

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
        return redirect("reviews:index")
    return render(request, "accounts/signin.html", {"form": form})

@login_required
def signout(request):
    logout(request)
    return redirect('accounts:signin')