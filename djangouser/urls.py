from django.conf.urls import patterns, include, url
from djangouser.views import Login,Logout

urlpatterns = patterns('',
    url(r'^login/$', Login.as_view()),
    url(r'^logout/$', Logout.as_view()),
)
