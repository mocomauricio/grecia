from django.conf.urls import url
from .autocomplete import *
from .views import *

urlpatterns = [
    url(
        '^pedido-autocomplete/$',
        PedidoAutocomplete.as_view(),
        name='pedido-autocomplete',
    ),

]
