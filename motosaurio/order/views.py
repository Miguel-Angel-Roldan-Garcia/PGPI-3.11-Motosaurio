from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.conf import settings

from cart.cesta import Cesta
from shop.models import Product

from .forms import OrderForm
from .models import Order, CartItem

import stripe

class CheckoutOrder(TemplateView):
    
    def get(self, request, *args, **kwargs):
        template_name = "checkout_order.html"
        context = {}

        form = OrderForm()

        if request.user.is_authenticated:
            user = request.user
            form["first_name"].initial = user.first_name
            form["email"].initial = user.email
            form["postal_code"].initial = user.direccion
            form["card_number"] .initial = user.tarjeta

        context["form"] = form
        context["cesta"] = Cesta(request)

        return render(request, template_name = template_name, context = context)
    
    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST)
        cesta = Cesta(request)

        if form.is_valid():
            if request.user.is_authenticated:
                user = request.user
            else:
                user = None

            order = Order(customer = user, \
                          first_name = form["first_name"].data, \
                          email = form["email"].data, \
                          direccion = form["direction"].data, \
                          cod_postal = form["postal_code"].data, \
                          tipo_pago = form["payment_type"].data, \
                          total_price = cesta.get_total_price()
                        )
            order.save()

            for k,v in cesta.cesta.items():
                cart_item = CartItem(item = Product.objects.get(id = k), quantity = v["quantity"], order = order)
                cart_item.save()

            if order.tipo_pago == "T":
                return redirect(f"/order/{order.id}/stripe")
            else:
                return redirect("dashboard")
        else:
            template_name = "checkout_order.html"
            context = {}

            context["form"] = form
            context["cesta"] = cesta
            return render(request, template_name = template_name, context = context)
        
class StripeCheckout(TemplateView):

    def get(self, request, order_id, *args, **kwargs):
        stripe.public_key = settings.STRIPE_PUBLIC_KEY
        order = Order.objects.get(id = order_id)

        context = {
            "stripe_public_key": stripe.public_key,
            "final_price": order.total_price,
            "order_id": order.id
        }

        return render(request, "stripe_checkout.html", context)

    def post(self, request, order_id, *args, **kwargs):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        token = request.POST.get('stripeToken')
        amount = Order.objects.get(id = order_id).total_price
        
        try:
            # Create a charge using the token and amount
            charge = stripe.Charge.create(
                amount=int(amount*100), # From eur to cents
                currency='eur',
                source=token,
                description=f'Cargo por el pedido con id {order_id}',
            )

            # Payment was successful
            # Perform additional actions (e.g., update database, send confirmation email)
            return redirect('dashboard')

        except stripe.error.CardError as e:
            # Card was declined
            error_message = str(e)
            return render(request, 'stripe_checkout.html', {'error_message': error_message})

        