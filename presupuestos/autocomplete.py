from dal import autocomplete
from django.db.models import Q

from .models import *

class PresupuestoAutocomplete(autocomplete.Select2QuerySetView):
	def get_queryset(self):
		# Don't forget to filter out results depending on the visitor !
		if not self.request.user.is_authenticated():
			return Presupuesto.objects.none()

		qs = Presupuesto.objects.filter(borrado=False)

		if self.q:
			qs = qs.filter(id__istartswith=self.q)

		return qs
