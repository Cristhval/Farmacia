from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Cliente, Empleado

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información Personal', {'fields': ('cedula', 'first_name', 'last_name', 'email', 'telefono')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Información Adicional', {'fields': ('rol',)}),
        ('Fechas Importantes', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'cedula', 'rol', 'email', 'telefono'),
        }),
    )
    list_display = ('username', 'rol', 'email', 'cedula', 'is_active')
    search_fields = ('username', 'email', 'cedula')
    list_filter = ('rol', 'is_staff', 'is_superuser', 'is_active')
    ordering = ('username',)


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):

    list_display = ('usuario', 'direccion')
    search_fields = ('usuario__username', 'usuario__email', 'direccion')
    autocomplete_fields = ('usuario',)


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):

    list_display = ('usuario', 'puesto')
    search_fields = ('usuario__username', 'usuario__email', 'puesto')
    autocomplete_fields = ('usuario',)
