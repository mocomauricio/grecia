from dal import autocomplete
from django.db.models import Q

from .models import *

class CategoriaAutocomplete(autocomplete.Select2QuerySetView):
	def get_queryset(self):
		# Don't forget to filter out results depending on the visitor !
		if not self.request.user.is_authenticated():
			return Categoria.objects.none()

		qs = Categoria.objects.filter(borrado=False)

		if self.q:
			qs = qs.filter(descripcion__icontains=self.q)

		return qs



class ArticuloAutocomplete(autocomplete.Select2QuerySetView):
	def get_queryset(self):
		# Don't forget to filter out results depending on the visitor !
		if not self.request.user.is_authenticated():
			return Articulo.objects.none()

		qs = Articulo.objects.filter(borrado=False)

		if self.q:
			qs = qs.filter( Q(descripcion__icontains=self.q) | Q(codigo__istartswith=self.q) ) 

		return qs
