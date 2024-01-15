from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from . import models
import json
from . import utils

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
    bills = models.Bill.objects.all()
    context = {
        'bills': bills
    }
    return render(request, 'bill.html', context)

def get_pdf(request, bill_id):
    bill = models.Bill.objects.get(id=bill_id)
    bill_products = models.BillProducts.objects.filter(bill__id=bill_id)
    return utils.generate_pdf(bill, bill_products)


def create_bill(request):
    if request.method == 'POST':
        data = json.loads(request.POST.get('data', None))
        if data is None:
            raise AttributeError
        
        bill = models.Bill.objects.create(total_price=data['total_price'])
        for item in data['items']:
            product = models.Product.objects.get(id=item['id'])
            product.count_in_stock -= item['count']
            product.save()
            models.BillProducts.objects.create(
                bill=bill,
                product=product,
                count=item['count'],
                total_price=item['total_price']
            )
        return redirect('create-bill')
    
        
    products = models.Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'create_bill.html', context)