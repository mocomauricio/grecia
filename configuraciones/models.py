from django.db import models

# Create your models here.

class Configuracion(models.Model):
	titulo_sistema = models.CharField(max_length=50, verbose_name="titulo del sistema", default="DemoSystem")
	notificar_cumpleanhos = models.BooleanField(default=True)
	notificar_entrega_pedidos = models.BooleanField(verbose_name="notificar entrega de pedidos", default=True)
	notificar_entrega_pedidos_faltantes = models.BooleanField(verbose_name="notificar entrega de pedidos faltantes", default=True)
	notificar_retiro_pedidos = models.BooleanField(verbose_name="notificar retiro de pedidos", default=True)
	notificar_retiro_pedidos_faltantes = models.BooleanField(verbose_name="notificar retiro de pedidos faltantes", default=True)
