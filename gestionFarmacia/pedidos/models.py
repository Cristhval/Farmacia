from django.db import models
from django.core.exceptions import ValidationError


from inventario.models import Inventario


class Pedido(models.Model):
    ESTADOS = [
        ('PENDIENTE', 'Pendiente'),
        ('EN_TRANSITO', 'En tránsito'),
        ('ENTREGADO', 'Entregado'),
        ('CANCELADO', 'Cancelado'),
        ('EN_PREPARACION', 'En preparación'),
        ('LISTO_PARA_RETIRO', 'Listo para retiro'),
    ]

    OPCIONES_ENTREGA = [
        ('RETIRO_SUCURSAL', 'Retiro en Sucursal'),
        ('ENVIO_DESTINO', 'Envío a Sucursal de Destino'),
    ]

    cliente = models.ForeignKey('usuarios.Cliente', on_delete=models.CASCADE, related_name="pedidos")
    sucursal_origen = models.ForeignKey('inventario.Sucursal', on_delete=models.CASCADE, related_name="pedidos_origen")
    sucursal_destino = models.ForeignKey('inventario.Sucursal', on_delete=models.CASCADE, related_name="pedidos_destino")
    estado = models.CharField(max_length=20, choices=ESTADOS, default='PENDIENTE')
    productos = models.ManyToManyField('inventario.Producto', through='PedidoProducto')
    opcion_entrega = models.CharField(max_length=20, choices=OPCIONES_ENTREGA, default='RETIRO_SUCURSAL')


    def actualizar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
        self.save()

    def calcular_total(self):
        total = 0
        for pp in self.pedidoproducto_set.all():
            total += pp.producto.precio * pp.cantidad
        return total

    def validar_stock(self):

        for producto_pedido in self.pedidoproducto_set.all():
            inventario = Inventario.objects.filter(
                sucursal=self.sucursal_origen,
                producto=producto_pedido.producto
            ).first()
            if not inventario or inventario.cantidad < producto_pedido.cantidad:
                raise ValidationError(
                    f"No hay suficiente stock de {producto_pedido.producto.nombre} en {self.sucursal_origen.nombre}."
                )

    def confirmar_venta(self):

        self.validar_stock()


        for producto_pedido in self.pedidoproducto_set.all():
            inventario = Inventario.objects.get(
                sucursal=self.sucursal_origen,
                producto=producto_pedido.producto
            )
            inventario.cantidad -= producto_pedido.cantidad
            inventario.save()


        if self.opcion_entrega == 'RETIRO_SUCURSAL':
            self.actualizar_estado('LISTO_PARA_RETIRO')
        elif self.opcion_entrega == 'ENVIO_DESTINO':
            self.actualizar_estado('EN_TRANSITO')

    def __str__(self):
        return f"Pedido {self.id} - {self.estado}"


class PedidoProducto(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey('inventario.Producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.producto.nombre} x {self.cantidad} (Pedido {self.pedido.id})"
