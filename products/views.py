from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from .models import Product, Category

# Create your views here.

def all_products(request):
    """ Return a page which shows all products """

    products = Product.objects.all()
    categories = None
    query = None


    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                products = None
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            products = products.filter(name__icontains=query, description__icontains=query)
    
    context = {
        'products': products,
        'query': query,
        'cur_categories': categories,
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
