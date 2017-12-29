from django.conf.urls import url
from .autocomplete import *
from .views import *

urlpatterns = [
    url(
        '^cliente-autocomplete/$',
        ClienteAutocomplete.as_view(),
        name='cliente-autocomplete',
    ),

]
