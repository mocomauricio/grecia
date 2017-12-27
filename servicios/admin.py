from django.contrib import admin
from django.contrib.admin.decorators import register
from extra.globals import separador_de_miles
from .models import *

# Register your models here.
@register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
	list_display  = ('descripcion', 'get_precio_unitario', 'borrado')
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

	def get_precio_unitario(self, obj):
		return separador_de_miles(obj.precio_unitario)
	get_precio_unitario.short_description = 'precio unitario'
