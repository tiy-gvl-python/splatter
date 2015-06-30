# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('splat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Painting',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('medium', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PaintingStyle',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='painting',
            name='style',
            field=models.ForeignKey(to='splat.PaintingStyle'),
        ),
        migrations.AddField(
            model_name='splat',
            name='painting',
            field=models.ForeignKey(to='splat.Painting', null=True),
        ),
    ]
