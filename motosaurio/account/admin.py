from django.contrib import admin
from django.contrib.auth.models import User

@admin.register(User)
class registerUser(admin.ModelAdmin):
    list_display = ['usuario', 'nombre', 'email',
                    'telefono', 'direccion', 'contraseña']
    list_editable = ['email', 'telefono','direccion']
    prepopulated_fields = {'slug': ('usuario',)}
