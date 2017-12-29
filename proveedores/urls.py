from django.conf.urls import url
from .autocomplete import *
from .views import *

urlpatterns = [
    url(
        '^proveedor-autocomplete/$',
        ProveedorAutocomplete.as_view(),
        name='proveedor-autocomplete',
    ),

]
