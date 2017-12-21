from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Funcionario(models.Model):
	nombre = models.CharField(max_length=200, verbose_name="nombre o razon social")
	cedula_identidad = models.CharField(max_length=10, verbose_name="cedula de identidad", null=True, blank=True)
	telefono = models.CharField(max_length=20, null=True, blank=True)
	celular = models.CharField(max_length=20, null=True, blank=True)
	direccion = models.CharField(max_length=200, null=True, blank=True)
	email = models.CharField(max_length=20, null=True, blank=True)
	fecha_nacimiento = models.DateField(verbose_name="fecha de nacimiento", null=True, blank=True)
	fecha_ingreso = models.DateField(verbose_name="fecha de ingreso", null=True, blank=True)
	salario = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
	borrado = models.BooleanField(default=False, editable=False)

	def get_edad(self):
		pass

	def get_antiguedad(self):
		pass

	def get_usuario(self):
		pass

	def __str__(self):
		return self.nombre

class FuncionarioUsuario(models.Model):
	funcionario = models.ForeignKey(Funcionario)
	usuario = models.ForeignKey(User, verbose_name="usuario asignado")

	def __str__(self):
		return self.usuario.username