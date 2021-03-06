"""avtozip URL Configuration."""

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from httpproxy.views import HttpProxy

from webstore.api.urls import webstore_api

from . import views


urlpatterns = [
    url(r'^$', views.dashboard_view, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(webstore_api.urls)),
    url(r'^webstore/', include('webstore.urls', namespace='webstore')),
    url(r'^rosetta/', include('rosetta.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^tecdoc/(?P<url>.*)$', HttpProxy.as_view(base_url=settings.PROXY_TECDOC_URL)),
]
