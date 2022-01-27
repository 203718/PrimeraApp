from django.url import re_path

from primerComponente.views import PrimerViewList

urlpatterns =[
    re_path{r'^lista/$', PrimerViewList.as.view()}
    re_path{r'^lista/(?P<pk>\d+)$', PrimerViewList.as.view()}
]