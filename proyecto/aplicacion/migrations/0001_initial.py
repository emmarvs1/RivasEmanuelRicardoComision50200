# Generated by Django 5.0.1 on 2024-02-29 21:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Abonado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('nAbonado', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Facturas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nAbonado', models.IntegerField()),
                ('nFactura', models.IntegerField()),
                ('monto', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('servicio', models.CharField(max_length=50)),
                ('pago', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nAbonado', models.IntegerField()),
                ('servicio', models.CharField(max_length=250)),
                ('servicioMonto', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nTicket', models.IntegerField()),
                ('fecha', models.DateField()),
                ('descrip', models.CharField(max_length=200)),
                ('nAbonado', models.IntegerField()),
                ('estado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='avatares')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
