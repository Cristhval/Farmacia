from django.contrib import admin
from .models import Producto, Sucursal, Inventario


class InventarioInline(admin.TabularInline):
    model = Inventario
    extra = 1


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio')
    search_fields = ('nombre',)
    list_filter = ('precio',)
    ordering = ('nombre',)
    inlines = [InventarioInline]


@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion')
    search_fields = ('nombre', 'direccion')
    ordering = ('nombre',)
    inlines = [InventarioInline]


@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ('producto', 'sucursal', 'cantidad')
    search_fields = ('producto__nombre', 'sucursal__nombre')
    list_filter = ('sucursal', 'producto')
    ordering = ('sucursal', 'producto')

