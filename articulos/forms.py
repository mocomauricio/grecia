from dal import autocomplete
from django import forms
from .models import *
from django.urls import reverse

class ArticuloForm(forms.ModelForm):
	class Meta:
		model = Articulo
		fields = '__all__'
		widgets = {
			"categoria": autocomplete.ModelSelect2(url='categoria-autocomplete'),
		}