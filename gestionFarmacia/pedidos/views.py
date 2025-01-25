from django.shortcuts import render, get_object_or_404
from .models import Pedido

def detalle_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    return render(request, 'pedidos/detalle_pedido.html', {'pedido': pedido})


def lista_pedidos(request):
    pedidos = Pedido.objects.all()  # Obtén todos los pedidos de la base de datos
    return render(request, 'pedidos/lista_pedidos.html', {'pedidos': pedidos})