from .models import Sucursal, Producto, Inventario
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

def lista_sucursales(request):
    sucursales = Sucursal.objects.all()
    return render(request, 'inventario/lista_sucursales.html', {'sucursales': sucursales})


def lista_productos(request):
    productos = Producto.objects.all()  # Obtener todos los productos
    return render(request, 'inventario/lista_productos.html', {'productos': productos})


def consultar_inventario(request):

    sucursal_id = request.GET.get('sucursal_id')

    sucursales = Sucursal.objects.all()

    if sucursal_id:  # Si se selecciona una sucursal
        return redirect('consultar_inventario_por_sucursal', sucursal_id=sucursal_id)


    inventario = Inventario.objects.select_related('sucursal', 'producto').all()
    return render(request, 'inventario/consultar_inventario.html', {
        'inventario': inventario,
        'sucursal': None,
        'titulo': "Inventario de Todas las Sucursales",
        'sucursales': sucursales
    })


def consultar_inventario_por_sucursal(request, sucursal_id):

    sucursal = get_object_or_404(Sucursal, id=sucursal_id)
    inventario = Inventario.objects.filter(sucursal=sucursal).select_related('producto')

    sucursales = Sucursal.objects.all()

    return render(request, 'inventario/consultar_inventario.html', {
        'inventario': inventario,
        'sucursal': sucursal,
        'titulo': f"Inventario de {sucursal.nombre}",
        'sucursales': sucursales
    })


def transferir_producto(request, sucursal_id):
    sucursal_origen = get_object_or_404(Sucursal, id=sucursal_id)
    productos = Producto.objects.filter(inventarios__sucursal=sucursal_origen)
    sucursales = Sucursal.objects.exclude(id=sucursal_id)

    if request.method == 'POST':
        producto_id = request.POST.get('producto')
        cantidad = int(request.POST.get('cantidad', 0))
        sucursal_destino_id = request.POST.get('sucursal_destino')

        producto = get_object_or_404(Producto, id=producto_id)
        sucursal_destino = get_object_or_404(Sucursal, id=sucursal_destino_id)

        inventario_origen = Inventario.objects.filter(
            sucursal=sucursal_origen, producto=producto
        ).first()
        inventario_destino, created = Inventario.objects.get_or_create(
            sucursal=sucursal_destino, producto=producto, defaults={'cantidad': 0}
        )

        if inventario_origen and inventario_origen.cantidad >= cantidad:
            inventario_origen.cantidad -= cantidad
            inventario_destino.cantidad += cantidad
            inventario_origen.save()
            inventario_destino.save()
            messages.success(request, f"{cantidad} unidades de {producto.nombre} transferidas a {sucursal_destino.nombre}")
        else:
            messages.error(request, f"No hay suficiente stock de {producto.nombre} en {sucursal_origen.nombre}")

        return redirect('transferir_producto', sucursal_id=sucursal_origen.id)

    return render(request, 'inventario/transferir_producto.html', {
        'sucursal_origen': sucursal_origen,
        'productos': productos,
        'sucursales': sucursales
    })