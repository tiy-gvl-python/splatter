# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import pandas as pd
from splat.models import Splat, Painting, PaintingStyle


def load_painting_data(apps, schema_editor):
    painting_df = pd.read_csv('painting_dataset.csv', names=["id", "painting_style", "medium"])

    for row in painting_df.iterrows():
        painting_obj = row[1]
        style_obj = PaintingStyle.objects.get(id=painting_obj.painting_style)
        Painting.objects.create(id=painting_obj.id, medium=painting_obj.medium, style=style_obj)


class Migration(migrations.Migration):

    dependencies = [
        ('splat', '0003_auto_20150630_1351'),
    ]

    operations = [
        migrations.RunPython(load_painting_data),
    ]
