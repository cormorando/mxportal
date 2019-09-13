from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages

from products.models import Product
from cart.cart import Cart
from cart.forms import AddProductForm


@require_POST
def cart_add(request, pk):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=pk)
    form = AddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add_product(product=product, quantity=cd['quantity'])

    return redirect('product-list')


def cart_remove(request, pk):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=pk)
    cart.remove_product(product)

    return redirect('product-list')


@require_POST
def cart_order(request):
    cart = Cart(request)
    # send email
    messages.success(request, 'Order submitted. Place check your email.')
    cart.delete_cart()

    return redirect('product-list')
