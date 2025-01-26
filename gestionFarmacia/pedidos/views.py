from django.shortcuts import render, get_object_or_404
from .models import Pedido, PedidoProducto
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from .forms import PedidoForm
from inventario.models import Producto
def detalle_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    return render(request, 'pedidos/detalle_pedido.html', {'pedido': pedido})


def lista_pedidos(request):
    pedidos = Pedido.objects.all()  # Obtén todos los pedidos de la base de datos
    return render(request, 'pedidos/lista_pedidos.html', {'pedidos': pedidos})


def confirmar_pedido(request, pedido_id):
    """
    Vista para confirmar un pedido y actualizar su estado.
    """
    pedido = get_object_or_404(Pedido, id=pedido_id)

    try:
        pedido.confirmar_venta()  # Asumiendo que ya tienes este metodo en tu modelo Pedido
        messages.success(request, f"El pedido {pedido.id} ha sido confirmado con éxito.")
    except Exception as e:
        messages.error(request, f"Error al confirmar el pedido: {str(e)}")

    return redirect('detalle_pedido', pedido_id=pedido.id)

def crear_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save()

            # Aquí puedes agregar la lógica para asociar productos al pedido
            productos = request.POST.getlist('productos')  # IDs de productos
            cantidades = request.POST.getlist('cantidades')  # Cantidades correspondientes
            for producto_id, cantidad in zip(productos, cantidades):
                producto = Producto.objects.get(id=producto_id)
                PedidoProducto.objects.create(pedido=pedido, producto=producto, cantidad=cantidad)

            return redirect('detalle_pedido', pedido_id=pedido.id)
    else:
        form = PedidoForm()

    productos = Producto.objects.all()  # Para seleccionar productos en la interfaz
    return render(request, 'pedidos/crear_pedido.html', {'form': form, 'productos': productos})

def mis_pedidos(request):
    """
    Vista para listar los pedidos de un cliente autenticado.
    """
    pedidos = Pedido.objects.filter(cliente=request.user.cliente)  # Filtra los pedidos del cliente autenticado
    return render(request, 'pedidos/mis_pedidos.html', {'pedidos': pedidos})

