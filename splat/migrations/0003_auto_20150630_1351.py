# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from splat.models import Splat, Painting, PaintingStyle


def load_painting_style_data(apps, schema_editor):
    with open('painting_styles_dataset.csv') as infile:
        data = infile.readlines()
        for painting_style in data:
            style_data = painting_style.split(',')
            PaintingStyle.objects.create(id=style_data[0], description=style_data[1])


class Migration(migrations.Migration):

    dependencies = [
        ('splat', '0002_auto_20150630_1336'),
    ]

    operations = [
        migrations.RunPython(load_painting_style_data),
    ]
