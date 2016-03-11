# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsentry',
            name='body',
            field=models.TextField(verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043d\u043e\u0432\u043e\u0441\u0442\u0438'),
        ),
        migrations.AlterField(
            model_name='newsentry',
            name='image',
            field=models.ImageField(upload_to=b'img/', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435', blank=True),
        ),
        migrations.AlterField(
            model_name='newsentry',
            name='tease',
            field=models.TextField(verbose_name='\u0410\u043d\u043e\u043d\u0441', blank=True),
        ),
    ]
