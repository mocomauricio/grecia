# Generated by Django 2.0 on 2017-12-27 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='proveedor',
            options={'permissions': (('view_proveedor', 'Puede ver la lista de proveedores'),), 'verbose_name_plural': 'proveedores'},
        ),
    ]
