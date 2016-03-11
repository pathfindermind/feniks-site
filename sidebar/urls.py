from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'feniks.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'sidebar', name='sidebar_index'),

]
