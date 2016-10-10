from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<pmid>[0-9]+)/$', views.detail, name='detail'),
	url(r'^(?P<pmid>[0-9]+)/tool$', views.tool, name='tool'),
	url(r'^(?P<pmid>[0-9]+)/not$', views.nott, name='not'),
	url(r'^(?P<pmid>[0-9]+)/ambiguous$', views.ambiguous, name='ambiguous'),
	url(r'^next/$', views.next, name='next'),
	url(r'^data/$', views.data, name='data'),
	url(r'^(?P<pmid>[0-9]+)/fulltextviewed$', views.fulltextviewed, name='fulltextviewed'),
	url(r'^(?P<pmid>[0-9]+)/settoolname/(?P<toolname>.+)$', views.settoolname, name='settoolname'),
]
