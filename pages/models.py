# -*- coding: utf-8 -*-
# Create your models here.
from django.db import models


class Slider(models.Model):
    title = models.CharField(u'Заголовок', max_length=255)
    image = models.ImageField(upload_to='img/', blank=True, verbose_name='Изображение')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'слайд'
        verbose_name_plural = u'Слайды'

class History(models.Model):
    title = models.CharField(u'Заголовок', max_length=255)
    image_one = models.ImageField(upload_to='img/', blank=True, verbose_name='Изображение 1')
    image_two = models.ImageField(upload_to='img/', blank=True, verbose_name='Изображение 2')
    text = models.TextField(u'Текст')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'страница истории'
        verbose_name_plural = u'страницы истории'
