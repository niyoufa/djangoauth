from django.conf.urls import patterns, include, url
from djangouser.auth_views import auth_login, auth_logout

urlpatterns = patterns('',
    url(r'^login/$', auth_login),
    url(r'^logout/$', auth_logout),
)
