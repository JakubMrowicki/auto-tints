from products.models import Category, Product
from django.conf import settings

def get_categories(request):
    """ Get a list of all available categories """
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return context


def cart_contents(request):
    cart_items = {}
    total = 0
    grand_total = total + settings.DELIVERY_CHARGE

    context = {
        'cart_items': cart_items,
        'total': total,
        'grand_total' : grand_total,
        'delivery_charge': settings.DELIVERY_CHARGE,
    }

    return context
