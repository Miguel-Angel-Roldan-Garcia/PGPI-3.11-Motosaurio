from django.urls import path
from . import views

urlpatterns = [
 path('', views.CheckoutOrder.as_view(), name='checkout'),
]