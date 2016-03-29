from django.conf.urls import patterns, url

urlpatterns = patterns('videos.views',
    url(r'^$', 'index', name='index'),
)
