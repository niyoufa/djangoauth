from django.conf.urls import patterns, include, url
from django.contrib import admin
import djangouser

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include("djangouser.urls")),
)
