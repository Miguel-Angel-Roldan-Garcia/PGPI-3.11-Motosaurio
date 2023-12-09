from django.urls import path
from . import views

app_name = "order"

urlpatterns = [
 path('', views.CheckoutOrder.as_view(), name='checkout'),
 path('<int:order_id>/stripe', views.StripeCheckout.as_view(), name='stripe_checkout'),
 path('my_orders/', views.ListOrdersUser.as_view(), name="list-orders-user"),
 path('tracking', views.Tracking.as_view(), name = 'tracking'),
 path('tracking/<int:order_id>', views.TrackingShow.as_view(), name='tracking_show')
]