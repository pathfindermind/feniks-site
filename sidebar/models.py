# -*- coding: utf-8 -*-
from django.db import models

class Slider(models.Model):
    title = models.CharField(u'Заголовок', max_length=255)
    image = models.ImageField(upload_to='img/', blank=True, verbose_name='Изображение')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'слайд'
        verbose_name_plural = u'Слайды'


class Link(models.Model):
    link = models.CharField(u'Ссылка на сторонний сайт', max_length=255)
    image = models.ImageField(upload_to='img/', blank=True, verbose_name='Баннер')

    def __unicode__(self):
        return self.link

    class Meta:
        verbose_name = u'Партнер'
        verbose_name_plural = u'Партнеры'
