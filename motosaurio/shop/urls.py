# shop/urls.py

from django.urls import path
from .views import ListProducts, ProductDetailView

app_name = 'shop'

urlpatterns = [
    path('', ListProducts.as_view(), name='dashboard'),
    path('product/<int:pk>/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    # Ajusta el path según tus necesidades
    # ...
]
