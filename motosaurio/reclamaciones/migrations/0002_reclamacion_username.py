# Generated by Django 4.1.13 on 2023-12-03 14:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reclamaciones", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="reclamacion",
            name="username",
            field=models.CharField(max_length=200, null=True, verbose_name="Título"),
        ),
    ]