from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignupForm, ProfileForm
from django.urls import path, include
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
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

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("products:product_list")
    else:
        form = AuthenticationForm()
    
    context = {
        "form":form
    }
    return render(request, 'accounts/login.html', context)
