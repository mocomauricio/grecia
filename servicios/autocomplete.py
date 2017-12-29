from dal import autocomplete
from django.db.models import Q

from .models import *

from dal import autocomplete
from django.db.models import Q

from .models import *

class ServicioAutocomplete(autocomplete.Select2QuerySetView):
	def get_queryset(self):
		# Don't forget to filter out results depending on the visitor !
		if not self.request.user.is_authenticated():
			return Servicio.objects.none()

		qs = Servicio.objects.filter(borrado=False)

		if self.q:
			qs = qs.filter(descripcion__icontains=self.q)

		return qs

