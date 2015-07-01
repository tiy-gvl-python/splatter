# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('splat', '0005_auto_20150630_1458'),
    ]

    operations = [
        migrations.CreateModel(
            name='Splatee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('sex', models.CharField(max_length=1)),
                ('occupation', models.IntegerField()),
                ('postal_code', models.IntegerField()),
                ('age', models.IntegerField()),
            ],
        ),
    ]
