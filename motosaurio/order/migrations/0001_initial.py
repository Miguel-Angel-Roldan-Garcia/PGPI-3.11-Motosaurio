# Generated by Django 4.2.7 on 2023-12-03 11:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo elecrónico')),
                ('direccion', models.CharField(max_length=200, verbose_name='Dirección')),
                ('cod_postal', models.IntegerField(verbose_name='Código postal')),
                ('tipo_pago', models.TextField(choices=[['Cr', 'Contrareembolso'], ['T', 'Tarjeta']], verbose_name='')),
                ('total_price', models.FloatField(default=0)),
                ('delivery_type', models.TextField(choices=[['D', 'A domicilio'], ['R', 'Recoger en tienda']], verbose_name='')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order')),
            ],
        ),
    ]