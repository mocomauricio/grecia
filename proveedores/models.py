from django.db import models

# Create your models here.
class Proveedor(models.Model):
	nombre = models.CharField(max_length=200, verbose_name="nombre o razon social")
	ruc = models.CharField(max_length=10, verbose_name="RUC", null=True, blank=True)
	telefono = models.CharField(max_length=20, null=True, blank=True)
	celular = models.CharField(max_length=20, null=True, blank=True)
	direccion = models.CharField(max_length=200, null=True, blank=True)
	email = models.CharField(max_length=100, null=True, blank=True)
	borrado = models.BooleanField(default=False, editable=False)

	class Meta:
		verbose_name_plural = 'proveedores'
		permissions = (
			("view_proveedor", "Puede ver la lista de proveedores"),
		)

	def __str__(self):
		return self.nombre
