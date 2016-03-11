# -*- coding: utf-8 -*-
from django import template
from news.models import NewsEntry

register = template.Library()


@register.inclusion_tag('news/titles.html')
def news_title(news):
    entries = NewsEntry.objects.all().order_by('-created_at')[:3]
    return {
        'entries': entries
    }
