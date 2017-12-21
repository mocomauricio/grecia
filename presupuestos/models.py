from django.db import models

# Create your models here.
class Presupuesto(models.Model):
	fecha_carga = models.DateField(auto_now_add=True)
	cliente = models.ForeignKey(User)
	salario = models.DecimalField(max_digits=15, decimal_places=2)
	borrado = models.BooleanField(default=False, editable=False)

	def __str__(self):
		return str(self.id)

class PresupuestoArticulo(models.Model):
	presupuesto = models.ForeignKey(Presupuesto)
	articulo = models.ForeignKey("articulos.Articulo")
	cantidad = models.DecimalField(max_digits=15, decimal_places=2)
	precio = models.DecimalField(max_digits=15, decimal_places=2)
	subtotal = models.DecimalField(max_digits=15, decimal_places=2)
	borrado = models.BooleanField(default=False, editable=False)

class PresupuestoArticulo(models.Model):
	presupuesto = models.ForeignKey(Presupuesto)
	servicio = models.ForeignKey("servicios.Servicio")
	cantidad = models.DecimalField(max_digits=15, decimal_places=2)
	precio = models.DecimalField(max_digits=15, decimal_places=2)
	subtotal = models.DecimalField(max_digits=15, decimal_places=2)
	borrado = models.BooleanField(default=False, editable=False)
