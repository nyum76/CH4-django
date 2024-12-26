from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignupForm, ProfileForm
from django.urls import path, include
from django.contrib.auth import login as auth_login
from django.contrib.auth import login as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from .models import User
# from products.models import Product


def signup(request):
    
    if request.method == "POST":
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('products:product_list')
    else:
            form = SignupForm()

    context = {
        "form":form
    }
    return render(request, 'accounts/signup.html', context)

@require_http_methods(["GET","POST"])
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect("products:product_list")
    else:
        form = AuthenticationForm()
    
    context = {
        "form":form
    }
    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('accounts:login')
