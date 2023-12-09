# Generated by Django 4.2.7 on 2023-12-06 18:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='estado',
            field=models.TextField(choices=[['P', 'Procesando'], ['A', 'Aceptado'], ['E', 'Enviado'], ['EN', 'Entregado']], default=['P', 'Procesando'], verbose_name='Estado'),
        ),
        migrations.AddField(
            model_name='order',
            name='fecha_creacion',
            field=models.DateField(default=datetime.date.today, verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_type',
            field=models.TextField(choices=[['D', 'A domicilio'], ['R', 'Recoger en tienda']], verbose_name='Tipo de envio'),
        ),
        migrations.AlterField(
            model_name='order',
            name='tipo_pago',
            field=models.TextField(choices=[['Cr', 'Contrareembolso'], ['T', 'Tarjeta']], verbose_name='Tipo de pago'),
        ),
    ]
