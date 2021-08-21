# Generated by Django 2.0.2 on 2021-07-11 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=20, unique=True, verbose_name='Título')),
                ('resume', models.TextField(max_length=500, verbose_name='Resumen')),
            ],
            options={
                'verbose_name': 'Notificacíon',
                'verbose_name_plural': 'Notificaciones',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('CEDULA CIUDADANIA', 'CEDULA CIUDADANÍA'), ('CEDULA EXTRANJERIA', 'CEDULA EXTRANJERÍA'), ('PASAPORTE', 'PASAPORTE'), ('OTRO', 'OTRO')], default='OTRO', max_length=50, verbose_name='Tipo de documento')),
                ('document', models.CharField(max_length=20, unique=True, verbose_name='Documento')),
                ('address', models.CharField(max_length=50, verbose_name='Dirección')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('phone', models.CharField(max_length=20, verbose_name='Teléfono')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
        ),
        migrations.AddField(
            model_name='notification',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User', verbose_name='Usuario'),
        ),
    ]
