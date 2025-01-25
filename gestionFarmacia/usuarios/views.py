from django.shortcuts import render
from .models import Cliente, Empleado

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'usuarios/lista_clientes.html', {'clientes': clientes})


def lista_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'usuarios/lista_empleados.html', {'empleados': empleados})