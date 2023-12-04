from django.db import models

class Reclamacion(models.Model):
    titulo = models.CharField('Título',max_length=200)
    descripcion = models.CharField('Descripción',max_length=1000)
    username = models.CharField('Username',max_length=200, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username