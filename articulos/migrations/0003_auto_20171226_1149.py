# Generated by Django 2.0 on 2017-12-26 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0002_auto_20171226_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='proveedores',
            field=models.ManyToManyField(blank=True, null=True, to='proveedores.proveedor'),
        ),
    ]