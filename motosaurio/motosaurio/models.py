from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator

class MiUsuario(AbstractUser):

    tipos_pago = [
        ["Cr", "Contrareembolso"],
        ["T", "Tarjeta"]
    ]

    tipos_envio = [
        ["D", "A domicilio"],
        ["R", "Recoger en tienda"]
    ]

    first_name = models.CharField('Nombre',max_length=200)
    email = models.CharField('Correo elecrónico',max_length=200)
    direccion = models.CharField('Dirección postal', max_length=200)
    codigo = models.IntegerField('Código postal',validators=[MaxValueValidator(99999)], null=True)
    tipo_pago = models.TextField("Tipo de pago", choices = tipos_pago,null=True)
    delivery_type = models.TextField("Tipo de envío", choices = tipos_envio,null=True)
    tarjeta = models.BigIntegerField('Tarjeta de crédito', null=True)

    def __str__(self):
        return self.username
    
    