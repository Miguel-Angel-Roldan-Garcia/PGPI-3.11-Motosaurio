# Generated by Django 4.2.7 on 2023-12-06 12:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("motosaurio", "0002_miusuario_codigo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="miusuario",
            name="codigo",
            field=models.IntegerField(
                null=True,
                validators=[django.core.validators.MaxValueValidator(99999)],
                verbose_name="Código postal",
            ),
        ),
    ]
