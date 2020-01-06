from django.http import HttpRequest
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.db import transaction

from .models import Product, Review
from .forms import ReviewForm


def product_list_view(request):
    template = 'app/product_list.html'
    products = Product.objects.all()

    context = {
        'product_list': products,
    }

    return render(request, template, context)

@transaction.atomic
def product_view(request, pk):
    template = 'app/product_detail.html'
    product = get_object_or_404(Product, id=pk)
    reviews = Review.objects.all().filter(product=product)

    session = request.session

    is_review_exists = False

    session.get(str(pk), False)
    form = ReviewForm
    if request.method == 'POST':
        # логика для добавления отзыва
        text = request.POST.get('text')
        new_review = Review.objects.create(text=text,
                                       product=product)
        session[str(pk)] = True

    if session.get(str(pk)):
        is_review_exists = True
    context = {
        'form': form,
        'product': product,
        'reviews': reviews,
        'session': session,
        'is_review_exists': is_review_exists
    }

    return render(request, template, context)
