from django.contrib import admin
from .models import Producto, Sucursal, Inventario


class InventarioInline(admin.TabularInline):
    """
    Permite editar el inventario directamente desde las páginas de Sucursal o Producto.
    """
    model = Inventario
    extra = 1  # Muestra un campo adicional para agregar más inventario


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio')  # Campos visibles en la lista
    search_fields = ('nombre',)  # Permite buscar por nombre
    list_filter = ('precio',)  # Agrega un filtro por precio
    ordering = ('nombre',)  # Ordena los productos alfabéticamente
    inlines = [InventarioInline]  # Agregar InventarioInline


@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion')  # Campos visibles en la lista
    search_fields = ('nombre', 'direccion')  # Permite buscar por nombre o dirección
    ordering = ('nombre',)  # Ordena las sucursales alfabéticamente
    inlines = [InventarioInline]  # Agregar InventarioInline


@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ('producto', 'sucursal', 'cantidad')  # Campos visibles en la lista
    search_fields = ('producto__nombre', 'sucursal__nombre')  # Permite buscar por producto o sucursal
    list_filter = ('sucursal', 'producto')  # Agrega filtros por sucursal y producto
    ordering = ('sucursal', 'producto')  # Ordena primero por sucursal, luego por producto
    # Si deseas que "cantidad" sea editable, elimina readonly_fields
    # readonly_fields = ('cantidad',)
