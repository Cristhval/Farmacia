from django.db import models

class Persona(models.Model):
    cedula = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)

    class Meta:
        abstract = True

    def obtener_informacion(self):
        return f"{self.nombre} - {self.email}"
class Cliente(Persona):
    direccion = models.CharField(max_length=255)

    def registrar_pedido(self):
        # Lógica para registrar un pedido
        pass

    def ver_pedidos(self):
        # Lógica para listar pedidos
        pass

class Empleado(Persona):
    rol = models.CharField(max_length=50)

    def gestionar_inventario(self):
        # Lógica para gestionar inventario
        pass

    def gestionar_pedido(self):
        # Lógica para gestionar pedidos
        pass
