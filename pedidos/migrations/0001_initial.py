# Generated by Django 2.0 on 2017-12-26 12:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('presupuestos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_estimada_entrega', models.DateField(verbose_name='fecha estimada de entrega')),
                ('fecha_entrega', models.DateField(null=True)),
                ('fecha_estimada_retiro', models.DateField(verbose_name='fecha estimada de retiro')),
                ('fecha_retiro', models.DateField(null=True)),
                ('direccion_evento', models.CharField(max_length=200, verbose_name='direccion del evento')),
                ('estado', models.IntegerField(choices=[(0, 'CANCELADO'), (1, 'PENDIENTE'), (2, 'ENTREGADO'), (3, 'RETIRADO')], default=1, editable=False)),
                ('creador', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('presupuesto', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='presupuestos.Presupuesto')),
            ],
            options={
                'permissions': (('view_pedido', 'Puede ver la lista de pedidos'), ('cancel_pedido', 'Puede cancelar un pedido'), ('deliver_pedido', 'Puede entregar un pedido'), ('withdraw_pedido', 'Puede retirar un pedido')),
            },
        ),
    ]
