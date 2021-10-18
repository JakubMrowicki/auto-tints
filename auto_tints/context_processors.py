from products.models import Category, Product
from django.conf import settings
from django.shortcuts import get_object_or_404

def get_categories(request):
    """ Get a list of all available categories """
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return context


def cart_contents(request):
    cart = request.session.get('cart', {})
    cart_items = []
    cart_items_count = 0
    total = 0

    if cart:
        for quantity in list(cart.values()):
            cart_items_count += int(quantity)

    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        total += product.price * int(quantity)
        cart_items.append({
            'product': product,
            'item_id': item_id,
            'quantity': quantity,
            'total_price': product.price * int(quantity)
        })
    
    grand_total = total + settings.DELIVERY_CHARGE

    context = {
        'cart_items': cart_items,
        'cart_items_count': cart_items_count,
        'total': total,
        'grand_total' : grand_total,
        'delivery_charge': settings.DELIVERY_CHARGE,
    }

    return context
