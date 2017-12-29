from django.conf.urls import url
from .autocomplete import *
from .views import *

urlpatterns = [
    url(
        '^presupuesto-autocomplete/$',
        PresupuestoAutocomplete.as_view(),
        name='presupuesto-autocomplete',
    ),

]
