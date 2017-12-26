from django.db import models
from django.contrib.auth.models import User

# Create your models here.
PEDIDO_CANCELADO = 0
PEDIDO_PENDIENTE = 1
PEDIDO_ENTREGADO = 2
PEDIDO_RETIRADO = 3
ESTADOS_DEL_PEDIDO = (
	(PEDIDO_CANCELADO, 'CANCELADO'),
	(PEDIDO_PENDIENTE, 'PENDIENTE'),
	(PEDIDO_ENTREGADO, 'ENTREGADO'),
	(PEDIDO_RETIRADO, 'RETIRADO'),
)

class Pedido(models.Model):
	presupuesto = models.ForeignKey("presupuestos.Presupuesto", editable=False, on_delete=models.CASCADE)
	fecha_estimada_entrega = models.DateField(verbose_name="fecha estimada de entrega")
	fecha_entrega = models.DateField(null=True, editable=True)
	fecha_estimada_retiro = models.DateField(verbose_name="fecha estimada de retiro")
	fecha_retiro = models.DateField(null=True, editable=True)
	direccion_evento = 	models.CharField(max_length=200, verbose_name="direccion del evento")
	estado = models.IntegerField(choices=ESTADOS_DEL_PEDIDO, default=PEDIDO_PENDIENTE, editable=False)
	creador = models.ForeignKey(User, null=True, editable=False, on_delete=models.CASCADE)
	
	class Meta:
		permissions = (
			("view_pedido", "Puede ver la lista de pedidos"),
			("cancel_pedido", "Puede cancelar un pedido"),
			("deliver_pedido", "Puede entregar un pedido"),
			("withdraw_pedido", "Puede retirar un pedido"),
		)

	def __str__(self):
		return str(self.id)

