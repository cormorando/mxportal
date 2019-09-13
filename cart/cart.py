from django.shortcuts import render, reverse
from decimal import Decimal
from django.conf import settings
from products.models import Product


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add_product(self, product, quantity):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'name': product.name, 'quantity': int(quantity), 'price': str(product.price)}
        else:
            self.cart[product_id]['quantity'] = int(quantity)
        self.save_cart()

    def remove_product(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save_cart()

    def save_cart(self):
        self.session[settings.CART_SESSION_ID] = self.cart

    def delete_cart(self):
        del self.session[settings.CART_SESSION_ID]

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
