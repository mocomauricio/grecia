from django.conf.urls import url
from .autocomplete import *
from .views import *

urlpatterns = [
    url(
        '^funcionario-autocomplete/$',
        FuncionarioAutocomplete.as_view(),
        name='funcionario-autocomplete',
    ),

]
