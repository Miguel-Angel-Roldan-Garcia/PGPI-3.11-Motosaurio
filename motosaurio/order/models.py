from django.db import models

from shop.models import Product
from motosaurio.models import MiUsuario
from datetime import date

# Create your models here.

class Order(models.Model):

    tipos_pago = [
        ["Cr", "Contrareembolso"],
        ["T", "Tarjeta"]
    ]

    tipos_envio = [
        ["D", "A domicilio"],
        ["R", "Recoger en tienda"]
    ]

    estados = [
        ['P','Procesando'], 
        ['A','Aceptado'], 
        ['E','Enviado'], 
        ['EN','Entregado']
    ]

    customer = models.ForeignKey(MiUsuario, null=True, on_delete=models.SET_NULL)
    first_name = models.CharField('Nombre', max_length=200)
    email = models.EmailField('Correo elecrónico')
    direccion = models.CharField('Dirección', max_length=200)
    cod_postal = models.IntegerField('Código postal')
    tipo_pago = models.TextField("Tipo de pago", choices = tipos_pago)
    total_price = models.FloatField(default=0)
    delivery_type = models.TextField("Tipo de envio", choices = tipos_envio)
    estado = models.TextField("Estado", choices=estados, default=estados[0])
    fecha_creacion=models.DateField("Fecha de creación", default=date.today)

    @property
    def legible_estado(self):
        for tipo in self.estados:
            if tipo[0] == self.estado:
                return tipo[1]
        return None

    def __str__(self):
        return "Order " + str(self.id)
    
    @property
    def legible_tipo_pago(self):
        for tipo in self.tipos_pago:
            if tipo[0] == self.tipo_pago:
                return tipo[1]
        return None
    
    @property
    def legible_tipo_envio(self):
        for tipo in self.tipos_envio:
            if tipo[0] == self.delivery_type:
                return tipo[1]
        return None

class CartItem(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
