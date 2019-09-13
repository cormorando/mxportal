from django.shortcuts import render, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin

from products.models import Product
from cart.forms import AddProductForm
from cart.cart import Cart


class ProductListView(LoginRequiredMixin, FormMixin, ListView):

    model = Product
    form_class = AddProductForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = Cart(self.request)

        return context


class ProductDetailView(LoginRequiredMixin, DetailView):

    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
