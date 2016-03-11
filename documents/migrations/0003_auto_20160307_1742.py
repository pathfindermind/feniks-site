# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_auto_20160307_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constituent',
            name='doc',
            field=models.FileField(upload_to=b'docs', blank=True),
        ),
    ]
