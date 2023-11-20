from typing import Any
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Product

class ListProducts(TemplateView):
    
    def get(self, request, *args, **kwargs):
        template_name = "product_list.html"
        
        name_query = request.GET.get('name', None)
        fabricante = request.GET.get('producer', None)
        tipo = request.GET.get('product_type', None)

        products = Product.objects.all()

        product_types = set(map(lambda p: p.product_type, products))
        producers = set(map(lambda p: p.producer, products))

        if fabricante and tipo:
            products = Product.objects.filter(producer = fabricante, product_type = tipo)
        elif fabricante:
            products = Product.objects.filter(producer = fabricante)
        elif tipo:
            products = Product.objects.filter(product_type = tipo)

        if name_query:
            products = [p for p in products if name_query in p.name]
 

        context = dict()
        context['products'] = products
        context['product_types'] = sorted(list(product_types))
        context['producers'] = sorted(set(producers))
        context['section'] = 'dashboard'
        return render(request, template_name=template_name, context = context)