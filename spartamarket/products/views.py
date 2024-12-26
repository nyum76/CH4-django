from django.shortcuts import render, redirect


def product_list(request):
    render(request, 'products/product_list.html')