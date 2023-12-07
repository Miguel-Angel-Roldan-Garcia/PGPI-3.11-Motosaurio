from django.urls import path
from . import views
app_name = 'reclamaciones'

urlpatterns = [
 path('', views.register, name='register'),
]