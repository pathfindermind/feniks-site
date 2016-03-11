# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0003_auto_20160307_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constituent',
            name='doc',
            field=models.FileField(upload_to=b'/docs/', blank=True),
        ),
    ]