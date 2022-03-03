from django.urls import re_path

#importando vistas
from Register.views import PrimerRegisterView, RegisterViewNew

urlpatterns = [
    re_path(r'^v1/register', PrimerRegisterView.as_view()),
    re_path(r'^v2/register', RegisterViewNew.as_view())
]