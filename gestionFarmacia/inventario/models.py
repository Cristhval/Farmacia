from django.db import models


class Sucursal(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)

    def consultar_inventario(self):
        # Lógica para consultar inventario
        pass

    def realizar_transferencia(self, producto, cantidad, sucursal_destino):
        # Lógica para transferir productos
        pass

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.FloatField()

    def actualizar_stock(self):
        # Lógica para actualizar stock
        pass

    def consultar_stock_por_sucursal(self, sucursal):
        # Lógica para consultar stock en una sucursal específica
        pass

class Inventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="inventarios")
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name="inventario")
    cantidad = models.IntegerField()

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad
        self.save()
