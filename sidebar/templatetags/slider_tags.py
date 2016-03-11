# -*- coding: utf-8 -*-
from django import template
from sidebar.models import Slider, Link

register = template.Library()


@register.inclusion_tag('sidebar/slider.html')
def sidebar_slider(sidebar):
    slides = Slider.objects.all()
    return {
        'slides': slides
    }
