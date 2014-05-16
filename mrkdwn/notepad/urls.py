from django.conf.urls import patterns, url

from notepad import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<note_id>\d+)/$', views.detail, name='detail')
)