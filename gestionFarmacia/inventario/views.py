from .models import Sucursal, Producto
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

def lista_sucursales(request):
    sucursales = Sucursal.objects.all()
    return render(request, 'inventario/lista_sucursales.html', {'sucursales': sucursales})


def lista_productos(request):
    productos = Producto.objects.all()  # Obtener todos los productos
    return render(request, 'inventario/lista_productos.html', {'productos': productos})


def consultar_inventario(request, sucursal_id):
    sucursal = get_object_or_404(Sucursal, id=sucursal_id)
    inventario = sucursal.consultar_inventario()
    return render(request, 'inventario/consultar_inventario.html', {'sucursal': sucursal, 'inventario': inventario})


def transferir_producto(request, sucursal_id):
    """
    Vista para transferir productos entre sucursales.
    """
    sucursal_origen = get_object_or_404(Sucursal, id=sucursal_id)

    if request.method == 'POST':
        producto_id = request.POST.get('producto')
        cantidad = int(request.POST.get('cantidad'))
        sucursal_destino_id = request.POST.get('sucursal_destino')

        producto = get_object_or_404(Producto, id=producto_id)
        sucursal_destino = get_object_or_404(Sucursal, id=sucursal_destino_id)

        try:
            sucursal_origen.realizar_transferencia(producto, cantidad, sucursal_destino)
            messages.success(request, f"Se transfirieron {cantidad} unidades de {producto.nombre} a {sucursal_destino.nombre}.")
        except ValueError as e:
            messages.error(request, str(e))

        return redirect('consultar_inventario', sucursal_id=sucursal_origen.id)

    productos = Producto.objects.all()
    sucursales = Sucursal.objects.exclude(id=sucursal_origen.id)
    return render(request, 'inventario/transferir_producto.html', {
        'sucursal_origen': sucursal_origen,
        'productos': productos,
        'sucursales': sucursales
    })