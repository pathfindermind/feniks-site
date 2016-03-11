# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Constituent(models.Model):
    title = models.CharField(u'Заголовок', max_length=255)
    doc = models.FileField(upload_to='docs/', blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'документ'
        verbose_name_plural = u'документы'
