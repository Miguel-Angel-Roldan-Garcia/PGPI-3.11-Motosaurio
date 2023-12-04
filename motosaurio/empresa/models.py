from django.db import models

class Empresa(models.Model):
    nombre = models.CharField('Nombre',max_length=200)
    email = models.CharField('Correo elecrónico',max_length=200)
    direccion = models.CharField('Dirección postal', max_length=200)
    telefono = models.BigIntegerField('Teléfono', null=True)
    descripcion = models.CharField('Sobre nosotros',max_length=500)

    def __str__(self):
        return self.nombre
