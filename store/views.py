from django.shortcuts import render, get_object_or_404
from .models import product
from category.models import category


# Create your views here.
def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(category, slug=category_slug)
        products = product.objects.filter(category=categories, is_available=True)
        count = products.count()
    else:
        products = product.objects.all().filter(is_available = True)
        count = products.count()

    context = {
        'products':products,
        'count':count,
    }
    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):
    try:
        product_details = product.objects.get(category__slug=category_slug, slug = product_slug)
    except Exception as e:
        raise e
    
    context = {
        'product_details':product_details,
    }
    return render(request, 'store/product_detail.html', context)