from django.conf.urls.defaults import *
from django.conf import settings
# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

from django.views.generic import list_detail
from candidaturas.models import Candidatura
from django.contrib.auth.models import User, UserManager


# INDEX
urlpatterns = patterns('',
(r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'index.html'}),
(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_DOC_ROOT, 'show_indexes': False}),)

# CANDIDATURAS
urlpatterns += patterns('',
    (r'^candidaturas/add', 'candidaturas.views.add'),
    (r'^candidaturas/rm/(?P<candidatura_id>\d+)/$', 'candidaturas.views.rm'),
    (r'^candidaturas/approve/(?P<candidatura_id>\d+)/$', 'candidaturas.views.approve'),
    (r'^candidaturas/(?P<candidatura_id>\d+)/$', 'candidaturas.views.detail'),
    (r'^candidaturas/$', 'candidaturas.views.candidatura_list'),
    (r'^candidaturas/cv/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.CV_DOC_ROOT, 'show_indexes': False}),
)

# UTILIZADORES
urlpatterns += patterns('',
    (r'^utilizadores/add', 'utilizadores.views.add'),
    (r'^utilizadores/near/(?P<user_id>\d+)/$', 'utilizadores.views.near'),
    (r'^utilizadores/(?P<user_id>\d+)/$', 'utilizadores.views.detail'),
    (r'^utilizadores/$', 'utilizadores.views.user_list'),
    (r'^utilizadores/login/$', 'django.contrib.auth.views.login',
                            {'template_name': 'utilizadores/login.html'}),
    (r'^utilizadores/logout/$', 'django.contrib.auth.views.logout',
                            {'template_name': 'utilizadores/logout.html'}),
)

# TRATAMENTOS
urlpatterns += patterns('',
    (r'^tratamentos/start/(?P<paciente_id>\d+)/(?P<fisioterapeuta_id>\d+)/$', 'tratamentos.views.start'),
    (r'^tratamentos/end/(?P<tratamento_id>\d+)/$', 'tratamentos.views.end'),
    (r'^tratamentos/(?P<tratamento_id>\d+)/$', 'tratamentos.views.detail'),
    (r'^tratamentos/$', 'tratamentos.views.tratamentos_list'),
    (r'^tratamentos/fichas/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.FICHAS_DOC_ROOT, 'show_indexes': False}),
)


# ADMIN
# urlpatterns += patterns('',
#     (r'^admin/', include(admin.site.urls)),
# )