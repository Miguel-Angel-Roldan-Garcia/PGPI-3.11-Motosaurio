from django.contrib.auth.models import AbstractUser
from django.db import models

class MiUsuario(AbstractUser):
    first_name = models.CharField('Nombre',max_length=200)
    email = models.CharField('Correo elecrónico',max_length=200)
    direccion = models.CharField('Dirección postal', max_length=200)
    tarjeta = models.BigIntegerField('Tarjeta de crédito', null=True)

    def __str__(self):
        return self.username
    
    