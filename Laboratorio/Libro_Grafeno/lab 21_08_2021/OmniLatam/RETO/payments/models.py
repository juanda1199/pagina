from django.db import models
from orders.models import Order


class Payment(models.Model):
    PAYMENT_TYPE_CHOICES = [
        ('PAGO CONTRAENTREGA', 'PAGO CONTRAENTREGA'),
        ('TARJETA CRÉDITO', 'TARJETA CRÉDITO'),
        ('TARJETA DÉBITO', 'TARJETA DÉBITO'),
        ('PAYPAL', 'PAYPAL'),
        ('PSE', 'PSE'),
    ]
    payment_type = models.CharField(max_length=50,
                                    choices=PAYMENT_TYPE_CHOICES,
                                    default='OTRO',
                                    verbose_name="Opcion de pago")
    payment_total = models.PositiveIntegerField(verbose_name="Total a pagar",)

    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"

    def __str__(self):
        return str(self.payment_total)


class PaymentOrder(models.Model):
    total_payment_order = models.PositiveIntegerField(
        verbose_name="Pago total de la orden")

    subtotal = models.PositiveIntegerField(verbose_name="Subtotal")
    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              verbose_name="Orden de venta")
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE,
                                verbose_name="Producto")

    class Meta:
        verbose_name = "Detalle del pago"
        verbose_name_plural = "Detalle de los pagos"
        unique_together = ['order', 'payment']

    def __str__(self):
        return str(self.order)
