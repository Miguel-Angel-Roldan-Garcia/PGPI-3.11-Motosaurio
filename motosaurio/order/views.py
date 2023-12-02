from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.conf import settings

from cart.cesta import Cesta

from .forms import OrderForm
from .models import Order, CartItem

# Create your views here.

class CheckoutOrder(TemplateView):
    
    def get(self, request, *args, **kwargs):
        template_name = "checkout_order.html"
        context = {}

        form = OrderForm()

        if request.user.is_authenticated:
            user = request.user
            form["first_name"].data = user.first_name
            form["email"].data = user.email
            form["postal_code"].data = user.direccion
            form["card_number"] .data = user.tarjeta

        context["form"] = form
        context["cesta"] = Cesta(request)

        stripe_public_key = settings.STRIPE_PUBLIC_KEY
        context["stripe_public_key"] = stripe_public_key

        return render(request, template_name = template_name, context = context)
    
    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST)

        if form.is_valid():
            if request.user.is_authenticated:
                user = request.user
            else:
                user = None

            order = Order(customer = user, \
                          first_name = form["first_name"].data, \
                          email = form["email"].data, \
                          direccion = form["direction"].data, \
                          cos_postal = form["postal_code"].data, \
                          tipo_pago = form[""]
                        )

            return redirect("dashboard")
        else:
            template_name = "checkout_order.html"
            context = {}

            stripe_public_key = settings.STRIPE_PUBLIC_KEY
            context["stripe_public_key"] = stripe_public_key

            context["form"] = form
            context["cesta"] = Cesta(request)
            return render(request, template_name = template_name, context = context)
        