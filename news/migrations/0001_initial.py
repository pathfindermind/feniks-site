# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('slug', models.SlugField(verbose_name='\u0427\u041f\u0423')),
                ('image', models.ImageField(upload_to=b'img/', verbose_name=b'Image', blank=True)),
                ('tease', models.TextField(verbose_name='\u0422\u0438\u0437\u0435\u0440', blank=True)),
                ('body', models.TextField(verbose_name='\u041a\u043e\u043d\u0442\u0435\u043d\u0442')),
                ('draft', models.BooleanField(default=False, verbose_name='\u0412 \u0447\u0435\u0440\u043d\u043e\u0432\u0438\u043a\u0438')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('published_at', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u0414\u0430\u0442\u0430 \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438')),
            ],
            options={
                'ordering': ('-published_at',),
                'verbose_name': '\u043d\u043e\u0432\u043e\u0441\u0442\u044c',
                'verbose_name_plural': '\u041d\u043e\u0432\u043e\u0441\u0442\u0438',
            },
        ),
    ]
