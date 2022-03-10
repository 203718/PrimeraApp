from django.urls import path, include, re_path

# Importaciones de vistas
from Profile.views import ProfileTablaView, ProfileTablaDetail, UserTablaView

urlpatterns = [
    re_path(r'^imagen/(?P<pk>\d+)',ProfileTablaDetail.as_view()),
    re_path(r'^imagen',ProfileTablaView.as_view()),
    re_path(r'^usuario/(?P<pk>\d+)',UserTablaView.as_view()),
]