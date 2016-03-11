# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sidebar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('link', models.CharField(max_length=255, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0441\u0442\u043e\u0440\u043e\u043d\u043d\u0438\u0439 \u0441\u0430\u0439\u0442')),
                ('image', models.ImageField(upload_to=b'img/', verbose_name=b'\xd0\x91\xd0\xb0\xd0\xbd\xd0\xbd\xd0\xb5\xd1\x80', blank=True)),
            ],
            options={
                'verbose_name': '\u041f\u0430\u0440\u0442\u043d\u0435\u0440',
                'verbose_name_plural': '\u041f\u0430\u0440\u0442\u043d\u0435\u0440\u044b',
            },
        ),
    ]
