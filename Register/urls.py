from django.urls import re_path

#importando vistas
from Register.views import PrimerRegisterView

urlpatterns = [
    re_path(r'^', PrimerRegisterView.as_view())
]