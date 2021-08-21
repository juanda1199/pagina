from django.db import models
from orders.models import Order


class City(models.Model):
    CHOICE_DEPARTAMENTOS = (
        ("Amazonas", "Amazonas"),
        ("Antioquia", "Antioquia"),
        ("Arauca", "Arauca"),
        ("Atlántico", "Atlántico"),
        ("Bolívar", "Bolívar"),
        ("Boyacá", "Boyacá"),
        ("Caldas", "Caldas"),
        ("Caquetá", "Caquetá"),
        ("Casanare", "Casanare"),
        ("Cauca", "Cauca"),
        ("Cesar", "Cesar"),
        ("Chocó", "Chocó"),
        ("Córdoba", "Córdoba"),
        ("Cundinamarca", "Cundinamarca"),
        ("Guainía", "Guainía"),
        ("Guaviare", "Guaviare"),
        ("Huila", "Huila"),
        ("La Guajira", "La Guajira"),
        ("Magdalena", "Magdalena"),
        ("Meta", "Meta"),
        ("Nariño", "Nariño"),
        ("NortedeSantander", "Norte de Santander"),
        ("Putumayo", "Putumayo"),
        ("Quindío", "Quindío"),
        ("Risaralda", "Risaralda"),
        ("SanAndrésyProvidencia", "San Andrés y Providencia"),
        ("Santander", "Santander"),
        ("Sucre", "Sucre"),
        ("Tolima", "Tolima"),
        ("ValledelCauca", "Valle del Cauca"),
        ("Vaupés", "Vaupés"),
        ("Vichada", "Vichada"),
        ("Bogotá", "Bogotá d C.")

    )

    name = models.CharField(max_length=20, verbose_name="Nombre", unique=True)
    state = models.CharField(max_length=50, verbose_name="Departamento",
                             choices=CHOICE_DEPARTAMENTOS, default="Meta")

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"

    def __str__(self):
        return self.name


class Shipment(models.Model):
    date_shipment = models.DateField(verbose_name="Fecha de Envío")
    date_received = models.DateField(verbose_name="Fecha de recepción")
    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              verbose_name="Orden de venta")
    city = models.ForeignKey(City, on_delete=models.CASCADE,
                             verbose_name="Ciudad")

    class Meta:
        verbose_name = "lista de envío"
        verbose_name_plural = "lista de envíos"

    def __str__(self):
        return str(self.order)
