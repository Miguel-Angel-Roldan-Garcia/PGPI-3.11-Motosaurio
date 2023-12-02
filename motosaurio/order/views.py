from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.conf import settings

from cart.cesta import Cesta

from .forms import OrderForm

# Create your views here.

class CheckoutOrder(TemplateView):
    
    def get(self, request, *args, **kwargs):
        template_name = "checkout_order.html"
        context = {}

        context["form"] = OrderForm()
        context["cesta"] = Cesta(request)

        return render(request, template_name = template_name, context = context)
    
    def post(self, request, *args, **kwargs):

        return redirect("dashboard")