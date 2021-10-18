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
    cart_items = request.session.get('cart', {})
    cart_items_count = 0
    total = 0
    grand_total = total + settings.DELIVERY_CHARGE

    if cart_items:
        for quantity in list(cart_items.values()):
            cart_items_count += int(quantity)

    context = {
        'cart_items': cart_items,
        'cart_items_count': cart_items_count,
        'total': total,
        'grand_total' : grand_total,
        'delivery_charge': settings.DELIVERY_CHARGE,
    }

    return context
