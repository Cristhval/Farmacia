from django.contrib import admin
from .models import Cliente, Empleado

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'direccion')
    search_fields = ('nombre', 'email', 'telefono')

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'rol')
    search_fields = ('nombre', 'email', 'rol')
