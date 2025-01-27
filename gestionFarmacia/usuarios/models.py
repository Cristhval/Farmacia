from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):

    cedula = models.CharField(max_length=20, unique=True, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)

    ROLES = [
        ('ADMIN', 'Administrador'),
        ('EMPLEADO', 'Empleado'),
        ('CLIENTE', 'Cliente'),
    ]
    rol = models.CharField(max_length=10, choices=ROLES, default='CLIENTE')

    def __str__(self):
        return f"{self.username} ({self.get_rol_display()})"


class Cliente(models.Model):

    usuario = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE
    )
    direccion = models.CharField(max_length=255)

    def registrar_pedido(self):

        pass

    def ver_pedidos(self):

        pass

    def __str__(self):
        return self.usuario.username


class Empleado(models.Model):

    usuario = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE
    )
    puesto = models.CharField(max_length=50)

    def gestionar_inventario(self):

        pass

    def gestionar_pedido(self):

        pass

    def __str__(self):
        return self.usuario.username
