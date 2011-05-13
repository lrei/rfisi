from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('candidaturas.views',
    (r'^candidaturas/$', 'index'),
    (r'^candidaturas/add', 'add'),
    (r'^candidaturas/(?P<candidatura_id>\d+)/$', 'detail'),
    (r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    (r'^admin/', include(admin.site.urls)),
)