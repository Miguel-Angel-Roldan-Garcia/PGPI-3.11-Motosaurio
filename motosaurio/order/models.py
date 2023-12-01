from django.db import models

# Create your models here.

class CartItem(models.model):
    item = models.ForeignKey(Product, on_delete=models.CAS)
    quantity = models.IntegerField()
    order = models.ForeignKey(Order)

class Order(models.model):
    customer = models.ForeignKey(User, null=True)
    order_id = models.IntegerField()

class AnonimusOrder(models.model):
    first_name = models.CharField('Nombre',max_length=200)
    email = models.CharField('Correo elecrónico',max_length=200)
    direccion = models.CharField('Dirección postal', max_length=200)
    order_id = models.IntegerField()