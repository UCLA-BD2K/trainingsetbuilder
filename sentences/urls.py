from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
#	url(r'^(?P<pmid>[0-9]+)/$', views.detail, name='detail'),
#	url(r'^(?P<pmid>[0-9]+)/tool$', views.tool, name='tool'),
]
