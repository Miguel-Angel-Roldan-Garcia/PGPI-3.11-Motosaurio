from django.contrib import admin
from inventario.models import *

class ProductoAdmin(admin.ModelAdmin):
	list_display = ('id', 'description', 'exist_stock', 'sell_price', 'last_cost', 'type')
	search_fields = ['description', 'exist_stock']

admin.site.register(Producto, ProductoAdmin)