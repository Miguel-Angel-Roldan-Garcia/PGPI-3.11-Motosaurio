from django.contrib import admin
from .models import MiUsuario

@admin.register(MiUsuario)
class MiUsuarioAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name','email','direccion','tarjeta']
    readonly_fields = ['username', 'first_name','email','direccion','tarjeta']