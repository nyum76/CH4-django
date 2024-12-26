from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products':products})
    

@login_required
def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('products:product_list')
    else:
        form = ProductForm()
    return render(request, 'products/product_create.html', {'form':form})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk) # 상품을 가져옴. 없으면 404 에러 발생
    product.views += 1 # 상품 조회 수를 증가시키고
    product.save() # 증가한 조회수 값 저장
    return render(request, 'products/product_detail.html', {"product":product})


@login_required
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk) # 상품을 가져옴. 없으면 404 에러 발생
    if product.user != request.user:
        return redirect('products:product_detail', pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products:product_detail', pk=pk)
    else:
        form = ProductForm(instance=product, initial={'hashtags_str':''.join(ht.name for ht in product.hashtags.all())})
        
    return render(request, 'products/product_form.html', {'form':form, 'product':product})

@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if product.user != request.user:
            return redirect('products:product_detail', pk=pk)
        
    if request.method == "POST":
        product.delete()
        return redirect('products:product_list')
    return render(request, 'products/product_detail.html', {'product':product})
