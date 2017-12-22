from django.db import models

# Create your models here.
class Cliente(models.Model):
	nombre = models.CharField(max_length=200, verbose_name="nombre o razon social")
	cedula_identidad = models.CharField(max_length=10, verbose_name="cedula de identidad", null=True, blank=True)
	ruc = models.CharField(max_length=10, verbose_name="RUC", null=True, blank=True)
	telefono = models.CharField(max_length=20, null=True, blank=True)
	celular = models.CharField(max_length=20, null=True, blank=True)
	direccion = models.CharField(max_length=200, null=True, blank=True)
	email = models.CharField(max_length=20, null=True, blank=True)
	borrado = models.BooleanField(default=False, editable=False)
	
	class Meta:
		permissions = (("view_cliente", "Puede ver la lista de clientes"))

	def __str__(self):
		return self.nombre
