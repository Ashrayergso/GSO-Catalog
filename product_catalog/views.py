```python
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Product
from .forms import ProductForm
from django.contrib import messages
from django.core.paginator import Paginator

def index(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 10) 
    page_number = request.GET.get('page')
    product_list = paginator.get_page(page_number)
    return render(request, 'product_catalog/index.html', {'product_list': product_list})

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_catalog/detail.html', {'product': product})

def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product created successfully.')
            return HttpResponseRedirect(reverse('product_catalog:index'))
    else:
        form = ProductForm()
    return render(request, 'product_catalog/create_product.html', {'form': form})

def update_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully.')
            return HttpResponseRedirect(reverse('product_catalog:detail', args=(product.id,)))
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_catalog/update_product.html', {'form': form})

def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        product.delete()
        messages.success(request, 'Product deleted successfully.')
        return HttpResponseRedirect(reverse('product_catalog:index'))
    return render(request, 'product_catalog/delete_product.html', {'product': product})
```