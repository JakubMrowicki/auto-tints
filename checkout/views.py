from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    """
    Return the checkout page
    """

    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, 'Your cart is empty, add some items to checkout.')
        return redirect(reverse('products'))
    
    form = OrderForm()

    context = {
        'order_form': form
    }

    return render(request, 'checkout/checkout.html', context)