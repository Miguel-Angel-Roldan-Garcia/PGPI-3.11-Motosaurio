from typing import Any
from django import http
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Product

class ListProducts(TemplateView):
    template_name = "product_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.all()
        context['products'] = products
        context['section'] = "dashboard"
        return context
    