# Generated by Django 2.0 on 2017-12-26 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Configuracion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_sistema', models.CharField(default='DemoSystem', max_length=50, verbose_name='titulo del sistema')),
                ('notificar_cumpleanhos', models.BooleanField(default=True)),
                ('notificar_entrega_pedidos', models.BooleanField(default=True, verbose_name='notificar entrega de pedidos')),
                ('notificar_entrega_pedidos_faltantes', models.BooleanField(default=True, verbose_name='notificar entrega de pedidos faltantes')),
                ('notificar_retiro_pedidos', models.BooleanField(default=True, verbose_name='notificar retiro de pedidos')),
                ('notificar_retiro_pedidos_faltantes', models.BooleanField(default=True, verbose_name='notificar retiro de pedidos faltantes')),
            ],
        ),
    ]
