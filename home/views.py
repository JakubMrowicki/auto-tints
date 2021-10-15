from django.shortcuts import render
from products.models import Category

# Create your views here.

def index(request):
    """ Return the home page which shows product categories """
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'home/index.html', context)