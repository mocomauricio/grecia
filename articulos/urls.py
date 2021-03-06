from django.conf.urls import url
from .autocomplete import *
from .views import *

urlpatterns = [
    url(
        '^categoria-autocomplete/$',
        CategoriaAutocomplete.as_view(),
        name='categoria-autocomplete',
    ),

    url(
        '^articulo-autocomplete/$',
        ArticuloAutocomplete.as_view(),
        name='articulo-autocomplete',
    ),

]
