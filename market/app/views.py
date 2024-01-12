from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from . import models

def home(request):
    search = request.GET.get('search', None)
    category_id = request.GET.get('category_id', '0')
    if category_id != '0':
        products = models.Product.objects.filter(category_id=category_id)
    elif search:
        products = models.Product.objects.filter(name__icontains = search)
    else:
        products = models.Product.objects.all()
    categories = models.Category.objects.all()
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'home.html', context)


def category(request):
    if request.method == 'POST':
        category = request.POST.get('category_name')
        models.Category.objects.create(name=category)
        return redirect('category')
    
    category = models.Category.objects.all()
    context = {
        'category': category
    }
    return render(request, 'category.html', context)


@require_POST
def delete_category(request, category_id):
    category = models.Category.objects.get(id=category_id)
    category.delete()
    return redirect('category')


def create_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        short_description = request.POST.get('short_description')
        unit = request.POST.get('unit')
        count_in_stock = request.POST.get('count_in_stock')
        price = request.POST.get('price')
        category = request.POST.get('category')
        
        models.Product.objects.create(
            name=name,
            short_description=short_description,
            unit=unit,
            count_in_stock=count_in_stock,
            price=price,
            category_id=category, 
        )

        return redirect('home')
    categories = models.Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'create_product.html', context)


@require_POST
def delete_product(request, product_id):
    product = models.Product.objects.get(id=product_id)
    product.delete()
    return redirect('home')

def bill(request):
    return render(request, 'bill.html')


def create_bill(request):
    products = models.Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'create_bill.html', context)