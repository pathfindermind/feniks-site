# -*- coding: utf-8 -*-

from .import models
from django.conf import settings
from django.shortcuts import get_object_or_404

from utils.views import object_list

VIDEOS_ON_PAGE = getattr(settings, 'VIDEOS_ON_PAGE', 8)


def index(request):
    qs = models.Video.objects.all()
    tag_name = request.GET.get('tag', None)
    tag = None
    if tag_name:
        tag = get_object_or_404(Tag, name=tag_name)
        qs = TaggedItem.objects.get_by_model(qs, tag)
    extra_context = {
        'tag': tag
    }
    return object_list(request, qs, VIDEOS_ON_PAGE,
                       template_name='videos/index.html',
                       extra_context=extra_context)
