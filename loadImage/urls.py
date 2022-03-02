from django.urls import re_path

from loadImage.views import PrimerViewList, PrimerViewDetail

urlpatterns =[
    re_path(r'^lista/$', PrimerViewList.as_view()),
    re_path(r'^lista/(?P<pk>\d+)$', PrimerViewDetail.as_view()),
]