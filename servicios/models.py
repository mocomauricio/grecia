from django.db import models

# Create your models here.
class Servicio(models.Model):
	descripcion = models.CharField(max_length=200)
	precio_unitario = models.DecimalField(max_digits=15, decimal_places=2)
	borrado = models.BooleanField(default=False, editable=False)

	class Meta:
		permissions = (
			("view_servicio", "Puede ver la lista de servicios"),
		)

	def __str__(self):
		return self.descripcion
