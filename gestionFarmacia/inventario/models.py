from django.db import models


class Sucursal(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)

    def consultar_inventario(self):
        """
        Retorna todos los registros de inventario relacionados con esta sucursal.
        """
        return self.inventario.all()

    def realizar_transferencia(self, producto, cantidad, sucursal_destino):
        """
        Transfiere productos de esta sucursal a otra sucursal.

        :param producto: Producto a transferir.
        :param cantidad: Cantidad a transferir.
        :param sucursal_destino: Sucursal destino de la transferencia.
        :raises ValueError: Si no hay suficiente stock en la sucursal origen.
        """
        # Verificar stock en la sucursal origen
        inventario_origen = self.inventario.filter(producto=producto).first()
        if not inventario_origen or inventario_origen.cantidad < cantidad:
            raise ValueError(f"No hay suficiente stock de {producto.nombre} en {self.nombre}")

        # Restar stock de la sucursal origen
        inventario_origen.cantidad -= cantidad
        inventario_origen.save()

        # Sumar stock a la sucursal destino
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
        """
        Actualiza el stock de este producto en la sucursal indicada.

        :param sucursal: Sucursal donde se actualiza el stock.
        :param cantidad: Cantidad a sumar al stock existente.
        """
        inventario = self.inventarios.filter(sucursal=sucursal).first()
        if inventario:
            inventario.cantidad += cantidad
            inventario.save()
        else:
            Inventario.objects.create(producto=self, sucursal=sucursal, cantidad=cantidad)

    def consultar_stock_por_sucursal(self, sucursal):
        """
        Consulta el stock de este producto en una sucursal específica.

        :param sucursal: Sucursal a consultar.
        :return: Cantidad disponible en la sucursal (0 si no hay registro).
        """
        inventario = self.inventarios.filter(sucursal=sucursal).first()
        return inventario.cantidad if inventario else 0

    def __str__(self):
        return self.nombre


class Inventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="inventarios")
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name="inventario")
    cantidad = models.IntegerField()

    def actualizar_cantidad(self, nueva_cantidad):
        """
        Actualiza la cantidad disponible en el inventario.

        :param nueva_cantidad: Nueva cantidad a establecer.
        """
        self.cantidad = nueva_cantidad
        self.save()

    def __str__(self):
        return f"{self.producto.nombre} en {self.sucursal.nombre}: {self.cantidad}"
