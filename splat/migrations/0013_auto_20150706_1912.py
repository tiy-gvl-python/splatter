# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('splat', '0012_auto_20150706_1853'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='splat',
            options={'ordering': ['-created', '-id']},
        ),
        migrations.AlterField(
            model_name='splat',
            name='splatee',
            field=models.ForeignKey(related_name='splats', to='splat.Splatee'),
        ),
    ]
