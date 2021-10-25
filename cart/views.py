from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from products.models import Product


def view_cart(request):
    """ View to return cart page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add item(s) to the shopping cart """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    messages.success(request, f'Added {product.name} to your cart.')
    request.session['cart'] = cart
    return redirect(redirect_url)


def edit_item(request, item_id):
    """ Remove item from cart """

    product = get_object_or_404(Product, pk=item_id)
    cart = request.session.get('cart', {})
    redirect_url = request.POST.get('redirect_url')

    if request.POST.get('update_button'):
        quantity = request.POST.get('quantity')
        if item_id in list(cart.keys()):
            messages.success(request, f'Updated quantity \
                                        of {product.name} to {quantity}.')
            cart[item_id] = quantity

    if request.POST.get('delete_button'):
        if item_id in list(cart.keys()):
            messages.success(request, f'Removed \
                                        {product.name} from your cart.')
            del cart[item_id]

    request.session['cart'] = cart
    return redirect(redirect_url)
