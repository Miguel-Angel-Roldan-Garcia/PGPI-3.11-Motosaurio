from django.contrib import admin
from .models import Order, CartItem

@admin.register(Order)
class registerOrder(admin.ModelAdmin):
    list_display = ['id', 'customer', 'first_name', 'email', 'direccion', 'cod_postal']


@admin.register(CartItem)
class registerCartItem(admin.ModelAdmin):
    list_display = ['item', 'quantity', 'order']

