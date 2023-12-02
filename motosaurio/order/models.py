from django.db import models

from shop.models import Product
from motosaurio.models import MiUsuario

# Create your models here.

class Order(models.Model):

    tipos_pago = [
        ["Cr", "Contrareembolso"],
        ["T", "Tarjeta"]
    ]

    customer = models.ForeignKey(MiUsuario, null=True, on_delete=models.SET_NULL)
    first_name = models.CharField('Nombre', max_length=200)
    email = models.EmailField('Correo elecrónico')
    direccion = models.CharField('Dirección', max_length=200)
    cod_postal = models.IntegerField('Código postal')
    tipo_pago = models.TextField("", choices = tipos_pago)
    total_price = models.FloatField(default=0)

    def __str__(self):
        return "Order " + str(self.id)

class CartItem(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
