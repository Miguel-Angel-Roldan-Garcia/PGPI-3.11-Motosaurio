# Generated by Django 4.1.13 on 2023-12-03 13:24

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Reclamacion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=200, verbose_name="Título")),
                (
                    "descripcion",
                    models.CharField(max_length=1000, verbose_name="Descripción"),
                ),
            ],
        ),
    ]
