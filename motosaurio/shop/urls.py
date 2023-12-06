from django.urls import path
from . import views


urlpatterns = [
 path('', views.sold_products_view, name='productos_vendidos'),
]