# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('splat', '0011_auto_20150706_1456'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='splat',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='splat',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 6, 18, 53, 32, 514976), auto_now_add=True),
            preserve_default=False,
        ),
    ]
