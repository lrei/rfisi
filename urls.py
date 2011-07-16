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
    url(r'^$', 'django.views.generic.simple.direct_to_template',
                            {'template':'index.html'}, name = 'index'),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_DOC_ROOT, 'show_indexes': False}),)

# CANDIDATURAS
urlpatterns += patterns('',
    url(r'^candidaturas/add', 'candidaturas.views.add'),
    url(r'^candidaturas/rm/(?P<candidatura_id>\d+)/$',
                            'candidaturas.views.rm'),
    url(r'^candidaturas/approve/(?P<candidatura_id>\d+)/$',
                            'candidaturas.views.approve'),
    url(r'^candidaturas/(?P<candidatura_id>\d+)/$',
                            'candidaturas.views.detail'),
    url(r'^candidaturas/$', 'candidaturas.views.candidatura_list',
                            name = 'candidaturas'),
    url(r'^candidaturas/cv/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.CV_DOC_ROOT, 'show_indexes': False}),
    url(r'^candidaturas/bi/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.BI_DOC_ROOT, 'show_indexes': False}),
)

# UTILIZADORES
urlpatterns += patterns('',
    url(r'^utilizadores/add', 'utilizadores.views.add'),
    url(r'^utilizadores/near/(?P<user_id>\d+)/$', 'utilizadores.views.near'),
    url(r'^utilizadores/(?P<user_id>\d+)/$', 'utilizadores.views.detail'),
    url(r'^utilizadores/$', 'utilizadores.views.user_list',
                            name = 'utilizadores'),
    url(r'^utilizadores/login/$', 'django.contrib.auth.views.login',
                            {'template_name': 'utilizadores/login.html'},
                            name = 'login'),
    url(r'^utilizadores/logout/$', 'django.contrib.auth.views.logout',
                            {'template_name': 'utilizadores/logout.html'},
                            name = 'logout'),
)

# TRATAMENTOS
urlpatterns += patterns('',
url(r'^tratamentos/start/(?P<paciente_id>\d+)/(?P<fisioterapeuta_id>\d+)/$',
                    'tratamentos.views.start'),
    url(r'^tratamentos/end/(?P<tratamento_id>\d+)/$',
                    'tratamentos.views.end'),
    url(r'^tratamentos/(?P<tratamento_id>\d+)/$', 'tratamentos.views.detail'),
    url(r'^tratamentos/$', 'tratamentos.views.tratamentos_list',
                            name = 'tratamentos'),
    url(r'^tratamentos/fichas/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.FICHAS_DOC_ROOT, 'show_indexes': False}),
)


# ADMIN
# urlpatterns += patterns('',
#     (r'^admin/', include(admin.site.urls)),
# )