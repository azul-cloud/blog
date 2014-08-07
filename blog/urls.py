from django.conf.urls import patterns, include, url

from azulblog import views


# create app prefix to prepend to the name attribute of the urlpatterns
app = 'azulblog-'

urlpatterns = patterns('',
    url(r'^$', views.home, name = app + "home"),
    url(r'post/(?P<pk>\d+)/(?P<slug>\S+)/$', views.post, name =  app + "post"),
    url(r'tag/(?P<pk>\d+)/(?P<slug>\S+)/$', views.tag, name =  app + "tag"),
    url(r'(?P<year>\d\d\d\d)/(?P<month>\d\d)/$', views.date, name =  app + "month"),
    url(r'(?P<year>[0-9]{4})/$', views.date, name =  app + "year"),
)
