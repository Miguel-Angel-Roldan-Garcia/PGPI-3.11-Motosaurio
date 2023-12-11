from typing import Any
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from cart.forms import CestaAddProductForm
from django.contrib.admin.views.decorators import staff_member_required
from order.models import CartItem, Order
from datetime import *
from django.db.models import Sum

from .forms import ProductForm
from .models import Product, ProductReview

class ListProducts(TemplateView):
    
    def get(self, request, *args, **kwargs):
        template_name = "product_list.html"
        
        name_query = request.GET.get('name', None)
        description_query = request.GET.get('desc', None)
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
            name_query = name_query.lower()
            products = [p for p in products if name_query in p.name.lower()]
            
        if description_query:
            description_query = description_query.lower()
            products = [p for p in products if description_query in p.description.lower()]
 
        context = dict()
        context['products'] = products
        context['product_types'] = sorted(list(product_types))
        context['producers'] = sorted(set(producers))
        context['section'] = 'dashboard'
        cesta_product_form = CestaAddProductForm
        context['cesta_product_form'] = cesta_product_form
        return render(request, template_name=template_name, context = context)


class ProductDetailView(TemplateView):
    template_name = "product_detail.html"

    def get(self, request, *args, **kwargs):
        product_id = kwargs.get('pk')
        product = get_object_or_404(Product, id=product_id)
        reviews = ProductReview.objects.filter(product=product)

        form_valoracion = ProductForm()
        form_cesta = CestaAddProductForm()

        context = {
            'product': product,
            'reviews': reviews,  # Agrega esto para pasar las revisiones al contexto
            'valoracion_form': form_valoracion,
            'cesta_product_form': form_cesta,
            'section': 'product_detail',
        }

        return render(request, template_name=self.template_name, context=context)


    def post(self, request, *args, **kwargs):
        product_id = kwargs.get('pk')
        product = get_object_or_404(Product, id=product_id)
        form_valoracion = ProductForm(request.POST)
        form_cesta = CestaAddProductForm(request.POST)

        try:
            if request.method == 'POST' and request.user.is_authenticated:
                if form_valoracion.is_valid():
                    rating = form_valoracion.cleaned_data['rating']
                    opinion = form_valoracion.cleaned_data['opinion']
                    print(f"Rating: {rating}, Opinion: {opinion}")

                    if opinion:
                        review = ProductReview.objects.create(product=product, rating=rating, opinion=opinion, user=request.user)
                        print("Review created successfully!")
                    
                    print(f"Rating: {rating}, Opinion: {opinion}")
                    return redirect('shop:product_detail', pk=product.pk)
                else:
                    print("Form is not valid. Errors:", form_valoracion.errors)
        except Exception as e:
            print(f"Error creating review: {e}")
        
        print("Reviews:", product.reviews.all())

        context = {
            'product': product,
            'valoracion_form': form_valoracion,
            'cesta_product_form': form_cesta,
            'section': 'product_detail',
        }
        cesta_product_form = CestaAddProductForm
        context['cesta_product_form'] = cesta_product_form

        return render(request, template_name=self.template_name, context=context)

     
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
