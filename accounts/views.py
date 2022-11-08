from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model, login, logout
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def index(request):
    users = get_user_model().objects.all()
    return render(request, "accounts/index.html", {"users": users})

def signup(request):
    form = CustomUserCreationForm(request.POST or None)
    if form.is_valid():
        login(request, form.save())
        return redirect("articles:index")
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
    return redirect('accounts:signin')

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

@login_required
def edit(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("accounts:detail", request.user.username)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/edit.html", context)

def delete(request):
    form = CheckPasswordForm(request.user)
    if request.method == 'POST':
        form = CheckPasswordForm(request.user, request.POST)
        if form.is_valid():
            request.user.delete()
            logout(request)
            return redirect('accounts:index')
    context = {
        'form': form,
    }
    return render(request, 'accounts/delete.html', context)