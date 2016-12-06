from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
import oembed
oembed.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'feniks.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('pages.urls')),
    url(r'^about/', include('pages.urls')),
    url(r'^documents/', include('documents.urls')),
    url(r'^gallery/', include('photos.urls')),
    url(r'^contacts/', include('feedback_app.urls')),
    url(r'^videos/', include('videos.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]


if settings.DEBUG:
    urlpatterns += patterns('',
       url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
           {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )


urlpatterns += patterns('',
    url(r'^captcha/', include('captcha.urls')),
)
