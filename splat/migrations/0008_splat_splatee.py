# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('splat', '0007_auto_20150701_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='splat',
            name='splatee',
            field=models.ForeignKey(default=1, to='splat.Splatee'),
            preserve_default=False,
        ),
    ]
