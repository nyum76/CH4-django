from django.shortcuts import render, redirect

def main_login(request):
    return redirect('accounts:login')