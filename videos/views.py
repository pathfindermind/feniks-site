# -*- coding: utf-8 -*-
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .import models
from django.conf import settings
from django.shortcuts import get_object_or_404, render_to_response


def index(request):
    qs = models.Video.objects.all()
    paginator = Paginator(qs, 3)
    page = request.GET.get('page')
    try:
        qs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        qs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        qs = paginator.page(paginator.num_pages)
    return render_to_response('videos/index.html', {'qs':qs})