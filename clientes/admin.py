from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import *

# Register your models here.
@register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
	list_display  = ('nombre', 'cedula_identidad', 'ruc', 'telefono', 'celular', 'direccion', 'email', 'borrado')
	list_display_links = ('nombre',)
	list_filter = ('borrado',)
	ordering = ['nombre']
	search_fields = ['nombre', '^cedula_identidad', '^ruc']
	list_per_page = 30
	actions = ['set_no_borrado']

	def set_no_borrado(modeladmin, request, queryset):
		queryset.update(borrado=False)

	set_no_borrado.short_description = 'marcar como no borrado'
