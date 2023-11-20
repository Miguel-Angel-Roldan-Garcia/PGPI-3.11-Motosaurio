from typing import Any
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Product

class ListProducts(TemplateView):
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     products = Product.objects.all()
    #     context['products'] = products
    #     context['section'] = 'dashboard'
    #     return context
    
    def get(self, request, *args, **kwargs):
        template_name = "product_list.html"
        
        name_query = request.GET.get('name', None)
        fabricante = request.GET.get('producer', None)
        tipo = request.GET.get('product_type', None)
        order = request.GET.get('order', None)

        products = Product.objects.all()

        if fabricante and tipo:
            products = Product.objects.filter(producer = fabricante, product_type = tipo)
        elif fabricante:
            products = Product.objects.filter(producer = fabricante)
        elif tipo:
            products = Product.objects.filter(product_type = tipo)
        elif order:
            products= Product.objects.order_by(str(order))

        if name_query:
            products = [p for p in products if name_query in p.name]
 

        context = dict()
        context['products'] = products
        context['section'] = 'dashboard'
        return render(request, template_name=template_name, context = context)