from django.urls import path
from . import views
app_name = 'empresa'

urlpatterns = [
 path('', views.empresa_detail, name='empresa_detail'),
]