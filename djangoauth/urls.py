from django.conf.urls import patterns, include, url
from django.contrib import admin
from djangouser.admin_views import user_view

urlpatterns = patterns('',
    url(r'^admin/auth/user/', user_view),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include("djangouser.urls")),
)
