from django.shortcuts import render, get_object_or_404
from .models import Product, Category

# Create your views here.

def all_products(request):
    """ Return a page which shows all products """

    products = Product.objects.all()
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
    context = {
        'products': products,
    }
    return render(request, 'products/index.html', context)


def product_detail(request, product_id):
    """ Return a product detail page """

    query = Product.objects.filter(pk=product_id)
    if query.exists():
        product = query.get()

        context = {
            'product': product,
        }
    else:
        context = {
            'product': None
        }

    return render(request, 'products/detail.html', context)
