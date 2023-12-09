from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.conf import settings
from django.db import transaction
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseNotFound

from motosaurio.models import MiUsuario
from cart.cesta import Cesta
from shop.models import Product

from .forms import OrderForm
from .models import Order, CartItem

import stripe
from decimal import Decimal

class CheckoutOrder(TemplateView):
    
    def get(self, request, *args, **kwargs):
        template_name = "checkout_order.html"
        context = {}
        
        order_created_id = request.session.get("order_created_id")
        if order_created_id:
            request.session["order_created_id"] = None
            request.session.modified = True
            try:
                Order.objects.get(id = order_created_id).delete()    
            except Order.DoesNotExist:
                pass

        form = OrderForm()

        if request.user.is_authenticated:
            user = request.user
            form["first_name"].initial = user.first_name
            form["email"].initial = user.email
            form["direction"].initial = user.direccion
            form["postal_code"].initial = user.codigo
            form["payment_type"].initial = user.payment_type
            form["delivery_type"].initial = user.delivery_type
            # form["card_number"] .initial = user.tarjeta

        context["form"] = form
        context["cesta"] = Cesta(request)

        return render(request, template_name = template_name, context = context)
    
    def post(self, request, *args, **kwargs):

        @transaction.atomic
        def create_order(user, form, cesta):
            delivery_type = form["delivery_type"]
            final_price = cesta.get_total_price()

            if final_price <= 30:
                if delivery_type.data == "D":
                    final_price += Decimal("4.99")
                elif delivery_type.data == "R":
                    final_price += Decimal("3.99")

            order = Order(customer = user, \
                          first_name = form["first_name"].data, \
                          email = form["email"].data, \
                          direccion = form["direction"].data, \
                          cod_postal = form["postal_code"].data, \
                          tipo_pago = form["payment_type"].data, \
                          total_price = final_price, \
                          delivery_type = delivery_type, \
                          estado = "P"
                        )
            order.save()

            for k,v in cesta.cesta.items():
                cart_item = CartItem(item = Product.objects.get(id = k), quantity = v["quantity"], order = order)
                cart_item.save()
            
            return order

        form = OrderForm(request.POST)
        cesta = Cesta(request)

        if form.is_valid():
            if request.user.is_authenticated:
                user = request.user
            else:
                user = None

            order_created_id = request.session.get("order_created_id")

            if order_created_id:
                try:
                    Order.objects.get(id = order_created_id).delete()
                except Order.DoesNotExist:
                    pass

            order = create_order(user, form, cesta)
            order_created_id = request.session["order_created_id"] = order.id
            request.session.modified = True

            if order.tipo_pago == "T":
                # Credit card
                return redirect(f"/order/{order.id}/stripe")
            else:
                # Contrareembolso
                # Empty cart and send confirmation email
                request.session["order_created_id"] = None
                request.session[settings.CART_SESSION_ID] = None
                request.session.modified = True
                
                if(request.user.is_authenticated):
                    send_confirmation_mail(request.user.first_name, request.user.email, order.id)
                elif(order.email != None):
                    send_confirmation_mail(order.first_name, order.email, order.id)

                return render(request, 'checkout_thanks.html', {"email":order.email})
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
        order =  Order.objects.get(id = order_id)
        amount = order.total_price
        email = order.email
        context = {"email":email}
        
        try:
            # Create a charge using the token and amount
            charge = stripe.Charge.create(
                amount=int(amount*100), # From eur to cents
                currency='eur',
                source=token,
                description=f'Cargo por el pedido con id {order.id}',
            )

            # Payment was successful
            # Empty cart and send confirmation email
            request.session["order_created_id"] = None
            request.session[settings.CART_SESSION_ID] = None
            request.session.modified = True

            if(request.user.is_authenticated):
                send_confirmation_mail(request.user.first_name, request.user.email, order.id)
            elif(order.email != None):
                send_confirmation_mail(order.first_name, order.email, order.id)

            return render(request, 'checkout_thanks.html', context)

        except stripe.error.CardError as e:
            # Card was declined
            error_message = str(e)

            stripe.public_key = settings.STRIPE_PUBLIC_KEY
            order = Order.objects.get(id = order_id)

            context = {
                "stripe_public_key": stripe.public_key,
                "final_price": order.total_price,
                "order_id": order.id,
                'error_message': error_message
            }
            
            return render(request, 'stripe_checkout.html', context)

@method_decorator(login_required(login_url='/account/login'), name='dispatch')
class ListOrdersUser(TemplateView):
    template_name = 'list_orders_user.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user
        orders = Order.objects.filter(customer = user)
        context["orders"] = list()

        for order in orders:
            context["orders"].append((order, list(CartItem.objects.filter(order = order))))

        return context
 
    
class Tracking(TemplateView):
    template_name = "tracking.html"
    
class TrackingShow(TemplateView):

    def get(self, request, order_id, *args, **kwargs):
        try:
            order = Order.objects.get(id = order_id)
        except:
            return HttpResponseNotFound("No se ha encontrado ningún pedido con ese identificador")
        
        context = {
            "order": order
        }
        
        return render(request, "tracking_show.html", context)
    
def send_confirmation_mail(username, email, id_pedido):
    try:
        order = Order.objects.get(id = id_pedido)
        items = CartItem.objects.filter(order = order)

        asunto = f'Confirmación de pedido #{id_pedido}'
        mensaje = f'Hola {username},\n\nGracias por realizar el pedido con id: #{id_pedido} con nosotros!.\n'
        mensaje += 'Tu pedido contiene los siguientes productos: \n\n'
        
        for ci in items:
            mensaje += f"{ci.quantity} x {ci.item.name}\n"

        mensaje += '\n¡Estamos procesando tu solicitud y la enviaremos a la dirección proporcionada!\n\nAtentamente, El equipo de Motosaurio.'

        sender_mail = 'motosaurio.project@outlook.com'

        send_mail(
            subject=asunto,
            message=mensaje,
            from_email=sender_mail,
            recipient_list=[email],
            fail_silently=False
        )

        return True  

    except Exception as e:
        print(f"Error al enviar el correo: {e}")
        return False
