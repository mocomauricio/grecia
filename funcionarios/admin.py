from django.contrib import admin
from django.contrib.admin.decorators import register
from extra.globals import separador_de_miles
from .models import *

# Register your models here.
@register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
	list_display  = ('get_full_name', 'cedula_identidad', 'telefono', 'celular', 'direccion', 'email', 'fecha_nacimiento', 'fecha_ingreso', 'get_salario', 'borrado')
	list_display_links = ('get_full_name',)
	list_filter = ('borrado',)
	ordering = ['nombres']
	search_fields = ['nombres', 'apellidos', '^cedula_identidad']
	list_per_page = 30
	actions = ['set_no_borrado', 'set_borrado']

	def set_no_borrado(modeladmin, request, queryset):
		queryset.update(borrado=False)
	set_no_borrado.short_description = 'marcar como no borrado'

	def set_borrado(modeladmin, request, queryset):
		queryset.update(borrado=True)
	set_borrado.short_description = 'marcar como borrado'

	def get_full_name(self, obj):
		return obj.get_full_name()
	get_full_name.short_description = 'funcionario'

	def get_salario(self, obj):
		return separador_de_miles(obj.salario)
	get_salario.short_description = 'salario'

@register(FuncionarioUsuario)
class FuncionarioUsuarioAdmin(admin.ModelAdmin):
	list_display  = ('funcionario', 'usuario')
	list_display_links = ('funcionario', 'usuario')
	list_per_page = 30
