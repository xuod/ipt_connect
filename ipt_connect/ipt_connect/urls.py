from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from ipt_connect.views import home

urlpatterns = [
    # Examples:
    # url(r'^$', 'ipt_connect.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^$', home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/', include('loginas.urls')),
    url(r'^FPT2018/', include('FPT2018.urls', namespace='FPT2018')),
]



admin.site.site_header = 'IPT administration'
