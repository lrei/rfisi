from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.views.generic import list_detail
from candidaturas.models import Candidatura

candidatura_info = {
    'queryset': Candidatura.objects.filter(aceite=False),
}

# CANDIDATURAS
urlpatterns = patterns('',
    (r'^candidaturas/add', 'candidaturas.views.add'),
    (r'^candidaturas/rm/(?P<candidatura_id>\d+)/$', 'candidaturas.views.rm'),
    (r'^candidaturas/(?P<candidatura_id>\d+)/$', 'candidaturas.views.detail'),
    (r'^candidaturas/$', list_detail.object_list, candidatura_info),
)

# UTILIZADORES
urlpatterns += patterns('',
    (r'^utilizadores/add_medico', 'utilizadores.views.add_medico'),
)


# ADMIN
urlpatterns += patterns('',
    (r'^admin/', include(admin.site.urls)),
)