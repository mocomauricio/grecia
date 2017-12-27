from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Presupuesto(models.Model):
	fecha_carga = models.DateField(auto_now_add=True, verbose_name="fecha de carga")
	cliente = models.ForeignKey(User, on_delete=models.CASCADE)
	total = models.DecimalField(max_digits=15, decimal_places=2)
	aprobado = models.BooleanField(default=False, editable=False)
	borrado = models.BooleanField(default=False, editable=False)
	
	class Meta:
		permissions = (
			("view_presupuesto", "Puede ver la lista de presupuesto"),
			("accept_presupuesto", "Puede aprobar un presupuesto"),
		)

	def __str__(self):
		return str(self.id)

class PresupuestoArticulo(models.Model):
	presupuesto = models.ForeignKey(Presupuesto, on_delete=models.CASCADE)
	articulo = models.ForeignKey("articulos.Articulo", on_delete=models.CASCADE)
	cantidad = models.DecimalField(max_digits=15, decimal_places=2)
	precio = models.DecimalField(max_digits=15, decimal_places=2)
	subtotal = models.DecimalField(max_digits=15, decimal_places=2)
	borrado = models.BooleanField(default=False, editable=False)

class PresupuestoServicio(models.Model):
	presupuesto = models.ForeignKey(Presupuesto, on_delete=models.CASCADE)
	servicio = models.ForeignKey("servicios.Servicio", on_delete=models.CASCADE)
	cantidad = models.DecimalField(max_digits=15, decimal_places=2)
	precio = models.DecimalField(max_digits=15, decimal_places=2)
	subtotal = models.DecimalField(max_digits=15, decimal_places=2)
	borrado = models.BooleanField(default=False, editable=False)
