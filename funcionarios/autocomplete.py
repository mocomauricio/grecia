from dal import autocomplete
from django.db.models import Q

from .models import *

class FuncionarioAutocomplete(autocomplete.Select2QuerySetView):
	def get_queryset(self):
		# Don't forget to filter out results depending on the visitor !
		if not self.request.user.is_authenticated():
			return Funcionario.objects.none()

		qs = Funcionario.objects.filter(borrado=False)

		if self.q:
			qs = qs.filter(Q(nombres__icontains=self.q) | Q(apellidos__icontains=self.q) |  Q(cedula_identidad__istartswith=self.q))

		return qs
