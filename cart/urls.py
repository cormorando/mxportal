from django.urls import path

from cart.views import cart_add, cart_remove, cart_order

urlpatterns = [
    path('add/<int:pk>', cart_add, name='cart-add'),
    path('remove/<int:pk>', cart_remove, name='cart-remove'),
    path('order/', cart_order, name='cart-order'),
]
