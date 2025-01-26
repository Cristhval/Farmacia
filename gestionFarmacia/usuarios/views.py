from django.contrib.auth.decorators import login_required
from .models import Cliente, Empleado
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistroUsuarioForm

def lista_clientes(request):
    """
    Vista para listar clientes.
    """
    # Optimiza la consulta cargando la relación con Usuario en una sola consulta SQL
    clientes = Cliente.objects.select_related('usuario').all()
    return render(request, 'usuarios/lista_clientes.html', {'clientes': clientes})


def lista_empleados(request):
    """
    Vista para listar empleados.
    """
    empleados = Empleado.objects.select_related('usuario').all()
    return render(request, 'usuarios/lista_empleados.html', {'empleados': empleados})


def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario registrado con éxito. ¡Ahora puedes iniciar sesión!')
            return redirect('login')  # Redirige al login después del registro
        else:
            messages.error(request, 'Hubo un error en el registro. Verifica los datos ingresados.')
    else:
        form = RegistroUsuarioForm()
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