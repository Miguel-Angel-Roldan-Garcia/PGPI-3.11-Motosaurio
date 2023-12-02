from django.urls import path
from . import views

urlpatterns = [
 path('', views.CheckoutOrder.as_view(), name='checkout'),
 path('<int:order_id>/stripe', views.StripeCheckout.as_view(), name='stripe_checkout')
]