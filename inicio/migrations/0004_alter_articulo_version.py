# Generated by Django 4.2 on 2023-04-27 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0003_articulo_cantidad_requerida'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='version',
            field=models.CharField(max_length=20),
        ),
    ]
