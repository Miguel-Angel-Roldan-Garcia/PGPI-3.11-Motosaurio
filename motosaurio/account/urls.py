from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from cart import views as cart_views
from shop import views as shop_views
from motosaurio import urls

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name= 'logout'),
    path('', include('django.contrib.auth.urls')),
    path('', shop_views.ListProducts.as_view(), name='dashboard'),
    path('profile/', views.profile, name='perfil'),
    path('register/', views.register, name='register'),
]