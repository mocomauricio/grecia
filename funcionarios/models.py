from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Funcionario(models.Model):
	nombres = models.CharField(max_length=200)
	apellidos =  models.CharField(max_length=200)
	cedula_identidad = models.CharField(max_length=10, verbose_name="cedula de identidad", null=True, blank=True)
	telefono = models.CharField(max_length=20, null=True, blank=True)
	celular = models.CharField(max_length=20, null=True, blank=True)
	direccion = models.CharField(max_length=200, null=True, blank=True)
	email = models.CharField(max_length=100, null=True, blank=True)
	fecha_nacimiento = models.DateField(verbose_name="fecha de nacimiento", null=True, blank=True)
	fecha_ingreso = models.DateField(verbose_name="fecha de ingreso", null=True, blank=True)
	salario = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
	borrado = models.BooleanField(default=False, editable=False)
	
	class Meta:
		permissions = (
			("view_funcionario", "Puede ver la lista de funcionarios"),
		)

	def get_edad(self):
		fecha_actual = date.today()
		edad = fecha_actual.year - self.fecha_nacimiento.year
		if((fecha_actual.month < self.fecha_nacimiento.month) or (fecha_actual.month == self.fecha_nacimiento.month) and (fecha_actual.day < self.fecha_nacimiento.day)):
			edad = edad - 1
		return edad

	"""
	def es_cumple(self):
		fecha_actual = date.today()
		if( (self.fecha_nacimiento.day == fecha_actual.day) and (self.fecha_nacimiento.month == fecha_actual.month) ):
			return True
		return False
	"""

	def get_antiguedad(self):
		fecha_actual = date.today()
		edad = fecha_actual.year - self.fecha_ingreso.year
		if((fecha_actual.month < self.fecha_ingreso.month) or (fecha_actual.month == self.fecha_ingreso.month) and (fecha_actual.day < self.fecha_ingreso.day)):
			edad = edad - 1
		return edad

	def get_usuario(self):
		funcionarios_usuarios = FuncionarioUsuario.objects.filter(funcionario_id=self.id)
		if funcionarios_usuarios.count() > 0:
			return funcionarios_usuarios[0]
		return None

	def get_full_name(self):
		return self.nombres + " " + self.apellidos

	def __str__(self):
		return self.get_full_name()

class FuncionarioUsuario(models.Model):
	funcionario = models.OneToOneField(Funcionario, on_delete=models.CASCADE)
	usuario = models.OneToOneField(User, verbose_name="usuario asignado", on_delete=models.CASCADE)

	class Meta:
		verbose_name = 'usuario asignado a un funcionario'
		verbose_name_plural = 'usuario asignado a un funcionario'
		permissions = (
			("can_assign_user", "Puede asignar un usuario a un funcionario"),
		)

	def __str__(self):
		return self.usuario.username
