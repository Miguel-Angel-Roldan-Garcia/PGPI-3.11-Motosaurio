from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator

class MiUsuario(AbstractUser):

    first_name = models.CharField('Nombre',max_length=200)
    email = models.CharField('Correo elecrónico',max_length=200)
    direccion = models.CharField('Dirección postal', max_length=200)
    codigo = models.IntegerField('Código postal',validators=[MaxValueValidator(99999)], default = 00000)
    tarjeta = models.BigIntegerField('Tarjeta de crédito', null=True)

    def __str__(self):
        return self.username
    
    