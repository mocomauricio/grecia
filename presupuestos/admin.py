from django.contrib import admin
from django.contrib.admin.decorators import register
from extra.globals import separador_de_miles
from .models import *

# Register your models here.
class PresupuestoArticuloInline(admin.TabularInline):
	model = PresupuestoArticulo
	extra = 1

class PresupuestoServicioInline(admin.TabularInline):
	model = PresupuestoServicio
	extra = 1

@register(Presupuesto)
class PresupuestoAdmin(admin.ModelAdmin):
	list_display  = ('id', 'cliente', 'fecha_carga', 'get_total', 'borrado')
	list_display_links = ('id', 'cliente',)
	list_filter = ('borrado',)
	ordering = ['-id']
	search_fields = ['nombre', '^id']
	list_per_page = 30
	actions = ['set_no_borrado', 'set_borrado']

	def get_total(self, obj):
		return separador_de_miles(obj.total)

	def set_no_borrado(modeladmin, request, queryset):
		queryset.update(borrado=False)
	set_no_borrado.short_description = 'marcar como no borrado'

	def set_borrado(modeladmin, request, queryset):
		queryset.update(borrado=True)
	set_borrado.short_description = 'marcar como borrado'

	inlines = [
		PresupuestoArticuloInline,
		PresupuestoServicioInline
	]