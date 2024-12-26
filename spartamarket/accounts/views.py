from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignupForm, ProfileForm
from django.urls import path, include
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from .models import User
from products.models import Product


def signup(request):
    
    if request.method == "POST":
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
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

@login_required
def profile(request, username):
    profile_user = get_object_or_404(User, username=username)
    # 사용자가 게시한 물품
    my_products = Product.objects.filter(user=profile_user)
    # 사용자가 찜한 물품
    liked_products = profile_user.liked_products.all()

    # 팔로잉
    # 로그인한 사용자(request.user) 가 해당 profile_user 를 팔로우하고 있는지 확인
    # True / False 반환
    is_following = request.user.follows.filter(pk=profile_user.pk).exists()
    
    context = {
        'profile_user': profile_user,
        'my_products': my_products,
        'liked_products': liked_products,
        'is_following': is_following,
    }
    return render(request, 'accounts/profile.html', context)

