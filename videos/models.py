# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

import oembed

class Video(models.Model):
    title = models.CharField(_(u'title'), max_length=500)
    video = models.URLField(_(u'video URL'))
    description = models.TextField()
    created = models.DateTimeField(_(u'created'), auto_now_add=True)

    class Meta:
        ordering = ['-created']
        verbose_name = _(u'video')
        verbose_name_plural = _(u'videos')

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('videos:index',)

    def video_embed_code(self, maxwidth=300, maxheight=225):
        try:
            resource = oembed.site.embed(self.video, maxwidth=maxwidth, maxheight=maxheight)
            return resource.get_data()['html']
        except (oembed.exceptions.OEmbedException, KeyError):
            return ''

    def video_preview_code(self):
        try:
            resource = oembed.site.embed(self.video, maxwidth=348, maxheight=261)
            return resource.get_data()['html']
        except (oembed.exceptions.OEmbedException, KeyError):
            return ''
