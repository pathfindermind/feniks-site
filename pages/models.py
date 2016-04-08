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

# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime

'''
class Category(models.Model):
    name = models.CharField(u'Название', max_length=50)
    slug = models.SlugField(u'ЧПУ')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'категорию'
        verbose_name_plural = u'Категории'

    def __unicode__(self):
        return u'%s' % self.name
'''

class EntryManager(models.Manager):

    def published(self):
        return self.filter(draft=False)

    def drafted(self):
        return self.filter(draft=True)


class NewsEntry(models.Model):

    title = models.CharField(u'Заголовок', max_length=50)
    slug = models.SlugField(u'ЧПУ')
    image = models.ImageField(u'Изображение', upload_to='img/', blank=True)
    tease = models.TextField(u'Анонс', blank=True)
    body = models.TextField(u'Текст новости')
    draft = models.BooleanField(u'В черновики', default=False)
    created_at = models.DateTimeField(u'Дата создания', default=datetime.now)
    published_at = models.DateTimeField(u'Дата публикации', default=datetime.now)
    #category = models.ForeignKey(Category, related_name='entries', verbose_name = "Категория")

    objects = EntryManager()

    class Meta:
        verbose_name = u'новость'
        verbose_name_plural = u'Новости'
        ordering = ('-published_at',)

    def __unicode__(self):
        return u'%s' % self.title

    @models.permalink
    def get_absolute_url(self):
        return ('news_details', (), {'year': self.published_at.year,
                                     'month': self.published_at.strftime('%m'),
                                     'day': self.published_at.strftime('%d'),
                                     'slug': self.slug})
