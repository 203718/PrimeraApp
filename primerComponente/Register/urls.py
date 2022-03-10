from django.urls import re_path

#importando vistas
from Register.views import RegisterViewNew
# from Register.views import PrimerRegisterView

urlpatterns = [
    # re_path(r'^v1/register', PrimerRegisterView.as_view()),
    re_path(r'^usuario', RegisterViewNew.as_view())
]