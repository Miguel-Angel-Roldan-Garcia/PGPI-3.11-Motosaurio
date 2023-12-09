from django.urls import path
from .views import ListProducts, ProductDetailView, sold_products_view

app_name = 'shop'

urlpatterns = [
    path('', ListProducts.as_view(), name='dashboard'),
    path('products_sold/', sold_products_view, name='productos_vendidos'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]
