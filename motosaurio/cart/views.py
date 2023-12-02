from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cesta import Cesta
from .forms import CestaAddProductForm
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from motosaurio.models import MiUsuario

@require_POST
def cesta_add(request, product_id):
    cesta = Cesta(request)
    product = get_object_or_404(Product, id=product_id)
    form = CestaAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cesta.add(product=product,
                quantity=cd['quantity'],
                override_quantity=cd['override'])
    return redirect('cesta:cesta_detail')

@require_POST
def cesta_remove(request, product_id):
    cesta = Cesta(request)
    product = get_object_or_404(Product, id=product_id)
    cesta.remove(product)
    return redirect('cesta:cesta_detail')

def cesta_detail(request):
 cesta = Cesta(request)
 for item in cesta:
    item['update_quantity_form'] = CestaAddProductForm(initial={
                                    'quantity': item['quantity'],
                                    'override': True})
 return render(request, 'cesta/detail.html', {'cesta': cesta})

def send_confirmation_mail(id_pedido):
    try:
      #  order = Pedido.objects.get(id=id_pedido) Quitar cuando tengamos el pedido 
        user = MiUsuario

        userName = user.username
        userMail = user.email

        asunto = f'Confirmación de pedido #{id_pedido}'
        mensaje = f'Hola {userName},\n\nGracias por realizar el pedido #{id_pedido} con nosotros!. ¡Estamos procesando tu solicitud y la enviaremos a la dirección proporcionada!\n\nGracias, El equipo de Motosaurio.'

        sender_mail = 'motosaurio.project@outlook.com'

        send_mail(
            asunto,
            mensaje,
            sender_mail,
            [userMail],
            fail_silently=False,
        )

        return True  

    except Exception as e:
        print(f"Error al enviar el correo: {e}")
        return False