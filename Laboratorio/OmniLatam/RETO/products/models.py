from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    stock = models.PositiveIntegerField(verbose_name="Cantidad disponible",
                                        blank=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.name
