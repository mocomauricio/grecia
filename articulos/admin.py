from django.contrib import admin
from django.contrib.admin.decorators import register
from extra.globals import separador_de_miles
from .models import *

# Register your models here.
@register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
	list_display  = ('descripcion', 'borrado')
	list_display_links = ('descripcion',)
	list_filter = ('borrado',)
	ordering = ['descripcion']
	search_fields = ['descripcion']
	list_per_page = 30
	actions = ['set_no_borrado', 'set_borrado']

	def set_no_borrado(modeladmin, request, queryset):
		queryset.update(borrado=False)
	set_no_borrado.short_description = 'marcar como no borrado'

	def set_borrado(modeladmin, request, queryset):
		queryset.update(borrado=True)
	set_borrado.short_description = 'marcar como borrado'


@register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
	list_display  = ('descripcion', 'categoria', 'get_existencia', 'get_precio_unitario', 'borrado')
	list_display_links = ('descripcion',)
	list_filter = ('borrado', 'categoria')
	ordering = ['descripcion']
	search_fields = ['descripcion']
	list_per_page = 30
	filter_horizontal = ('proveedores',)
	actions = ['set_no_borrado', 'set_borrado']

	def set_no_borrado(modeladmin, request, queryset):
		queryset.update(borrado=False)
	set_no_borrado.short_description = 'marcar como no borrado'

	def set_borrado(modeladmin, request, queryset):
		queryset.update(borrado=True)
	set_borrado.short_description = 'marcar como borrado'

	def get_existencia(self, obj):
		return separador_de_miles(obj.existencia)
	get_existencia.short_description = 'existencia'

	def get_precio_unitario(self, obj):
		return separador_de_miles(obj.precio_unitario)
	get_precio_unitario.short_description = 'precio unitario'

