from django.conf.urls import url
from .autocomplete import *
from .views import *

urlpatterns = [
    url(
        '^servicio-autocomplete/$',
        ServicioAutocomplete.as_view(),
        name='servicio-autocomplete',
    ),

]
