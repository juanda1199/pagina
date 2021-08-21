from django.db import models
from products.models import Product
from users.models import User


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name="Usuario")
    date_order = models.DateField(verbose_name="Fecha")
    order_total = models.PositiveIntegerField(verbose_name="Total")

    class Meta:
        verbose_name = "Orden"
        verbose_name_plural = "Ordenes"

    def __str__(self):
        return str(self.user)


class OrderDetail(models.Model):
    price = models.PositiveIntegerField(verbose_name="Precio")
    quantity = models.PositiveIntegerField(verbose_name="Cantidad")
    iva = models.FloatField(verbose_name="IVA")
    subtotal = models.PositiveIntegerField(verbose_name="Subtotal")
    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              verbose_name="Orden de venta")
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                verbose_name="Producto")

    class Meta:
        verbose_name = "Detalle de la orden"
        verbose_name_plural = "Detalle de las ordenes"
        unique_together = ['order', 'product']

    def __str__(self):
        return self.product
