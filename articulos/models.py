from django.db import models


# Create your models here.
class Categoria(models.Model):
	descripcion = models.CharField(max_length=100)
	borrado = models.BooleanField(default=False, editable=False)

	class Meta:
		permissions = (("view_categoria", "Puede ver la lista de categorias"))

	def __str__(self):
		return self.descripcion

class Articulo(models.Model):
	descripcion = models.CharField(max_length=200)
	categoria = models.ForeignKey(Categoria)
	existencia = models.IntegerField(default=0, editable=False)
	precio_unitario = models.DecimalField(max_digits=15, decimal_places=2)
	proveedores = models.ManyToManyField('proveedores.Proveedor')
	borrado = models.BooleanField(default=False, editable=False)

	class Meta:
		permissions = (("view_articulo", "Puede ver la lista de articulos"))

	def __str__(self):
		return self.descripcion