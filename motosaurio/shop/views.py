from typing import Any
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from cart.forms import CestaAddProductForm
from django.contrib.admin.views.decorators import staff_member_required
from order.models import CartItem, Order
from datetime import *
from django.db.models import Sum

from .models import Product

class ListProducts(TemplateView):
    
    def get(self, request, *args, **kwargs):
        template_name = "product_list.html"
        
        name_query = request.GET.get('name', None)
        fabricante = request.GET.get('producer', None)
        tipo = request.GET.get('product_type', None)
        order = request.GET.get('order', None)

        products = Product.objects.all()

        product_types = set(map(lambda p: p.product_type, products))
        producers = set(map(lambda p: p.producer, products))

        if fabricante and tipo:
            products = Product.objects.filter(producer = fabricante, product_type = tipo)
        elif fabricante:
            products = Product.objects.filter(producer = fabricante)
        elif tipo:
            products = Product.objects.filter(product_type = tipo)
        elif order:
            products= Product.objects.order_by(str(order))

        if name_query:
            name_query = name_query.upper()
            products = [p for p in products if name_query in p.name]
 

        context = dict()
        context['products'] = products
        context['product_types'] = sorted(list(product_types))
        context['producers'] = sorted(set(producers))
        context['section'] = 'dashboard'
        cesta_product_form = CestaAddProductForm
        context['cesta_product_form'] = cesta_product_form
        return render(request, template_name=template_name, context = context)

     
@staff_member_required
def sold_products_view(request):
    template_name = "sold_products.html"
    date_from = datetime.now() - timedelta(days=60)
    orders = Order.objects.filter(fecha_creacion__gte=date_from)
    cart_items = CartItem.objects.filter(order__in=orders)
    products = Product.objects.filter(cartitem__in=cart_items).annotate(total_sold=Sum('cartitem__quantity'))

    context = dict()
    context['products'] = products

    return render(request, template_name=template_name, context=context)