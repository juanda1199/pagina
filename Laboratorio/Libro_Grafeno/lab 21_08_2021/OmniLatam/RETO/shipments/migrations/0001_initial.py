# Generated by Django 2.0.2 on 2021-07-11 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='Nombre')),
                ('state', models.CharField(choices=[('Amazonas', 'Amazonas'), ('Antioquia', 'Antioquia'), ('Arauca', 'Arauca'), ('Atlántico', 'Atlántico'), ('Bolívar', 'Bolívar'), ('Boyacá', 'Boyacá'), ('Caldas', 'Caldas'), ('Caquetá', 'Caquetá'), ('Casanare', 'Casanare'), ('Cauca', 'Cauca'), ('Cesar', 'Cesar'), ('Chocó', 'Chocó'), ('Córdoba', 'Córdoba'), ('Cundinamarca', 'Cundinamarca'), ('Guainía', 'Guainía'), ('Guaviare', 'Guaviare'), ('Huila', 'Huila'), ('La Guajira', 'La Guajira'), ('Magdalena', 'Magdalena'), ('Meta', 'Meta'), ('Nariño', 'Nariño'), ('NortedeSantander', 'Norte de Santander'), ('Putumayo', 'Putumayo'), ('Quindío', 'Quindío'), ('Risaralda', 'Risaralda'), ('SanAndrésyProvidencia', 'San Andrés y Providencia'), ('Santander', 'Santander'), ('Sucre', 'Sucre'), ('Tolima', 'Tolima'), ('ValledelCauca', 'Valle del Cauca'), ('Vaupés', 'Vaupés'), ('Vichada', 'Vichada'), ('Bogotá', 'Bogotá d C.')], default='Meta', max_length=50, verbose_name='Departamento')),
            ],
            options={
                'verbose_name': 'Ciudad',
                'verbose_name_plural': 'Ciudades',
            },
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_shipment', models.DateField(verbose_name='Fecha de Envío')),
                ('date_received', models.DateField(verbose_name='Fecha de recepción')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shipments.City', verbose_name='Ciudad')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Order', verbose_name='Orden de venta')),
            ],
            options={
                'verbose_name': 'lista de envío',
                'verbose_name_plural': 'lista de envíos',
            },
        ),
    ]
