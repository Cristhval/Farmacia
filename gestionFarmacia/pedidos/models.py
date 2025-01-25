from django.db import models


class Pedido(models.Model):
    ESTADOS = [
        ('PENDIENTE', 'Pendiente'),
        ('EN_TRANSITO', 'En tránsito'),
        ('ENTREGADO', 'Entregado'),
        ('CANCELADO', 'Cancelado'),
        ('EN_PREPARACION', 'En preparación'),
        ('LISTO_PARA_RETIRO', 'Listo para retiro'),
    ]

    cliente = models.ForeignKey('usuarios.Cliente', on_delete=models.CASCADE, related_name="pedidos")
    sucursal_origen = models.ForeignKey('inventario.Sucursal', on_delete=models.CASCADE, related_name="pedidos_origen")
    sucursal_destino = models.ForeignKey('inventario.Sucursal', on_delete=models.CASCADE, related_name="pedidos_destino")
    estado = models.CharField(max_length=20, choices=ESTADOS, default='PENDIENTE')
    productos = models.ManyToManyField('inventario.Producto', through='PedidoProducto')

    def actualizar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
        self.save()

    def __str__(self):
        return f"Pedido {self.id} - {self.estado}"

    def calcular_total(self):
        total = 0
        for pp in self.pedidoproducto_set.all():
            total += pp.producto.precio * pp.cantidad
        return total


class PedidoProducto(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey('inventario.Producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.producto.nombre} x {self.cantidad} (Pedido {self.pedido.id})"