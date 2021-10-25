from django.shortcuts import render
from products.models import Category


def index(request):
    """ Return the home page which shows product categories """
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'home/index.html', context)
