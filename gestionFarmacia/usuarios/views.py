from django.contrib.auth.decorators import login_required

from .models import Cliente, Empleado, Usuario
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'usuarios/lista_clientes.html', {'clientes': clientes})


def lista_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'usuarios/lista_empleados.html', {'empleados': empleados})


def registro(request):
    """
    Vista para registrar nuevos usuarios.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            # Puedes asignar un rol predeterminado, por ejemplo, CLIENTE
            usuario.rol = 'CLIENTE'
            usuario.save()
            messages.success(request, 'Usuario registrado con éxito. ¡Ahora puedes iniciar sesión!')
            return redirect('login')
        else:
            messages.error(request, 'Hubo un error en el registro. Verifica los datos ingresados.')
    else:
        form = UserCreationForm()
    return render(request, 'usuarios/registro.html', {'form': form})

@login_required
def perfil(request):
    """
    Vista para mostrar el perfil del usuario autenticado.
    """
    return render(request, 'usuarios/perfil.html', {'user': request.user})
@login_required
def dashboard(request):
    """
    Vista para mostrar el panel de usuario.
    Diferencia entre roles (administrador, empleado, cliente).
    """
    return render(request, 'usuarios/dashboard.html', {'user': request.user})