from django.contrib import admin
from .models import Pedido, PedidoProducto

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'sucursal_origen', 'sucursal_destino', 'estado', 'opcion_entrega')
    search_fields = ('cliente__nombre', 'sucursal_origen__nombre', 'sucursal_destino__nombre', 'opcion_entrega')
    list_filter = ('estado', 'sucursal_origen', 'sucursal_destino', 'opcion_entrega')  # Agregado filtro por opción de entrega

@admin.register(PedidoProducto)
class PedidoProductoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'producto', 'cantidad')
    search_fields = ('pedido__id', 'producto__nombre')
