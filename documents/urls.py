from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'feniks.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^constituent_documents/', 'documents.views.constituent', name='constituent'),
]
