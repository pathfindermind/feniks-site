# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xbc\xd0\xb0:')),
                ('name', models.CharField(max_length=100, verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f:')),
                ('phone', models.CharField(max_length=100, verbose_name=b'\xd0\x9d\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd1\x82\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x84\xd0\xbe\xd0\xbd\xd0\xb0:')),
                ('text', models.TextField(verbose_name=b'\xd0\xa1\xd0\xbe\xd0\xbe\xd0\xb1\xd1\x89\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5:')),
            ],
            options={
                'verbose_name': '\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435',
                'verbose_name_plural': '\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f',
            },
        ),
    ]
