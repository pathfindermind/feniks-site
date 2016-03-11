# -*- coding: utf-8 -*-
from django import template
from sidebar.models import Link

register = template.Library()

@register.inclusion_tag('sidebar/links.html')
def sidebar_links(sidebar):
    links = Link.objects.all()
    return {
        'links': links
    }
