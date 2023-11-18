# -*- encoding: utf-8 -*-
from django.db import models

TYPE_CHOICES = (
	('RU', 'RUEDAS'),
	('MO', 'MOTOR'),
	('FR', 'FRENOS'),
	('FI', 'FILTROS'),
	('EM', 'EMBRAGUE'),
	('ES', 'ESCAPE'),
	('MA', 'MANILLAR'),
	('OT', 'OTROS')
)

PRODUCER_CHOICES = (
	('KW', 'KAWASAKI'), 
	('HO', 'HONDA'), 
	('YA', 'YAMAHA'), 
	('DU', 'DUCATI'), 
	('KY', 'KYMCO'),
	('OT', 'OTROS') 
)

class Producto(models.Model):
	description = models.CharField(max_length=255, verbose_name='Descripción')
	product_type= models.CharField(max_length=255, verbose_name='Tipo de producto', choices=TYPE_CHOICES)
	producer 	= models.CharField(max_length=255, verbose_name='fabricante', choices=PRODUCER_CHOICES)
	sell_price  = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio de venta')
	exist_stock = models.IntegerField(default=0, verbose_name='Existencia')
	create_date = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return self.description