# Generated by Django 5.2.1 on 2025-06-04 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_pais_cliente_nacimiento_cliente_pais_origen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pais',
            name='nombre',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
