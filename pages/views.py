from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order


def faq(request):
    """ Return FAQ page """

    return render(request, 'pages/faq.html')


def profile(request):
    """ Return Profile page """

    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your details have been updated.')
    form = UserProfileForm(instance=profile)
    orders = profile.orders.all().order_by('-date')
    context = {
        'orders': orders,
        'form': form
    }
    return render(request, 'pages/profiles/profile.html', context)


def order_history(request, order_number):
    """ Return order history page """
    order = get_object_or_404(Order, order_number=order_number)
    context = {
        'order': order
    }
    return render(request, 'pages/profiles/order_history.html', context)