from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cesta import Cesta
from .forms import CestaAddProductForm
from django.shortcuts import render, redirect

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
    return redirect('shop:dashboard')

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

