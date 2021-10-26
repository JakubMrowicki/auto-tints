from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product, Category, Review
from pages.models import UserProfile
from .forms import ProductForm, ReviewForm


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
                messages.error(request, "You didn't enter any \
                                         search criteria!")
                return redirect(reverse('products'))

            products = products.filter(name__icontains=query,
                                       description__icontains=query)

    context = {
        'products': products,
        'query': query,
        'cur_categories': categories,
    }
    return render(request, 'products/index.html', context)


def product_detail(request, product_id):
    """ Return a product detail page """

    query = Product.objects.filter(pk=product_id)
    reviews = Review.objects.filter(product=product_id).order_by('-date')
    form = ReviewForm()
    if query.exists():
        product = query.get()

        context = {
            'product': product,
            'reviews': reviews[:5],
            'form': form
        }
    else:
        context = {
            'product': None
        }

    return render(request, 'products/detail.html', context)


@login_required
def add_review(request, product_id):
    """
    Add a product review
    """

    user = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)
    already_reviewed = Review.objects.filter(user=user, product=product)
    if not already_reviewed:
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.user = user
                form.product = product
                form.save()
                messages.success(request, 'Thank you for your review!')
            else:
                messages.error(request, 'Something went wrong with your review.\
                                        Try again.')
        else:
            messages.info(request, 'Invalid action.')
    else:
        messages.warning(request, 'You already left a review \
            for this product.')
    return redirect(reverse('detail_page', args=[product.id]))


@login_required
def delete_review(request, review_id):
    """
    Delete a review
    """

    review = get_object_or_404(Review, pk=review_id)
    product = review.product
    review_owner = review.user.user == request.user
    if review_owner or request.user.is_superuser:
        review.delete()
        messages.success(request, 'Review deleted successfully.')
    else:
        messages.error(request, 'You cannot delete this review')
    return redirect(reverse('detail_page', args=[product.id]))


@login_required
def add_product(request):
    """
    Allow admin to add product
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, this is a restricted area.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product saved successfully.')
            return redirect(reverse('detail_page', args=[product.id]))
        else:
            messages.error(request, 'Please ensure the form is valid.')
    else:
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'products/add_product.html', context)


@login_required
def edit_product(request, product_id):
    """
    Allow admin to edit a product
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, this is a restricted area.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully.')
            return redirect(reverse('detail_page', args=[product.id]))
        else:
            messages.error(request, 'Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
    context = {
        'form': form,
        'product': product
    }
    return render(request, 'products/edit_product.html', context)


@login_required
def delete_product(request, product_id):
    """
    Allow admin to delete a product
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, this is a restricted area.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted successfully.')
    return redirect(reverse('home'))
