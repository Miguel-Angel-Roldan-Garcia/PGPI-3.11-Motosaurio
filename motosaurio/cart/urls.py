from django.urls import path
from . import views
app_name = 'cesta'

urlpatterns = [
 path('', views.cesta_detail, name='cesta_detail'),
 path('add/<int:product_id>/', views.cesta_add, name='cesta_add'),
 path('remove/<int:product_id>/', views.cesta_remove, 
 name='cesta_remove'),
]