from django.contrib import admin
from .models import Reclamacion

@admin.register(Reclamacion)
class ReclamacionAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'descripcion','username','created']
    readonly_fields = ['titulo', 'descripcion','username','created']
