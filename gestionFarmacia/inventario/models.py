from django.db import models


class Sucursal(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)

    def consultar_inventario(self):

        return self.inventario.all()

    def realizar_transferencia(self, producto, cantidad, sucursal_destino):

        inventario_origen = self.inventario.filter(producto=producto).first()
        if not inventario_origen or inventario_origen.cantidad < cantidad:
            raise ValueError(f"No hay suficiente stock de {producto.nombre} en {self.nombre}")

        inventario_origen.cantidad -= cantidad
        inventario_origen.save()

        inventario_destino, created = Inventario.objects.get_or_create(
            producto=producto,
            sucursal=sucursal_destino,
            defaults={'cantidad': 0}
        )
        inventario_destino.cantidad += cantidad
        inventario_destino.save()

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.FloatField()

    def actualizar_stock(self, sucursal, cantidad):
        inventario = self.inventarios.filter(sucursal=sucursal).first()
        if inventario:
            inventario.cantidad += cantidad
            inventario.save()
        else:
            Inventario.objects.create(producto=self, sucursal=sucursal, cantidad=cantidad)

    def consultar_stock_por_sucursal(self, sucursal):
        inventario = self.inventarios.filter(sucursal=sucursal).first()
        return inventario.cantidad if inventario else 0

    def __str__(self):
        return self.nombre


class Inventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="inventarios")
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name="inventario")
    cantidad = models.IntegerField()

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad
        self.save()

    def __str__(self):
        return f"{self.producto.nombre} en {self.sucursal.nombre}: {self.cantidad}"
