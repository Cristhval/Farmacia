from django.shortcuts import render
from .models import Sucursal, Producto

def lista_sucursales(request):
    sucursales = Sucursal.objects.all()
    return render(request, 'inventario/lista_sucursales.html', {'sucursales': sucursales})


def lista_productos(request):
    productos = Producto.objects.all()  # Obtener todos los productos
    return render(request, 'inventario/lista_productos.html', {'productos': productos})