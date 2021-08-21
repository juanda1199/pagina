from django.db import models


class User(models.Model):
    DOCUMENT_TYPE = [
        ('CEDULA CIUDADANIA', 'CEDULA CIUDADANÍA'),
        ('CEDULA EXTRANJERIA', 'CEDULA EXTRANJERÍA'),
        ('PASAPORTE', 'PASAPORTE'),
        ('OTRO', 'OTRO'),
    ]

    type = models.CharField(max_length=50, choices=DOCUMENT_TYPE,
                            default='OTRO', verbose_name="Tipo de documento")
    document = models.CharField(max_length=20, verbose_name="Documento",
                                unique=True)
    address = models.CharField(max_length=50, verbose_name="Dirección")
    name = models.CharField(max_length=50, verbose_name="Nombre")
    phone = models.CharField(max_length=20, verbose_name="Teléfono")

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return self.name


class Notification(models.Model):
    tittle = models.CharField(max_length=20, verbose_name="Título", unique=True)
    resume = models.TextField(max_length=500, verbose_name="Resumen")
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name="Usuario")

    class Meta:
        verbose_name = "Notificación"
        verbose_name_plural = "Notificaciones"

    def __str__(self):
        return self.tittle

