from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import *

# Register your models here.
@register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
	list_display  = ('nombre', 'ruc', 'telefono', 'celular', 'direccion', 'email', 'borrado')
	list_display_links = ('nombre',)
	list_filter = ('borrado',)
	ordering = ['nombre']
	search_fields = ['nombre', '^ruc']
	list_per_page = 30
	actions = ['set_no_borrado', 'set_borrado']

	def set_no_borrado(modeladmin, request, queryset):
		queryset.update(borrado=False)
	set_no_borrado.short_description = 'marcar como no borrado'

	def set_borrado(modeladmin, request, queryset):
		queryset.update(borrado=True)
	set_borrado.short_description = 'marcar como borrado'
