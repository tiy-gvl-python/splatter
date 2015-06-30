# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import pandas as pd
from splat.models import Splat, Painting, PaintingStyle


def load_splat_data(apps, schema_editor):
    splat_df = pd.read_csv('splat_dataset.csv', names=["id", "message", "painting"])
    splat_df.fillna(0, inplace=True)

    for row in splat_df.iterrows():
        splat_obj = row[1]
        splat_instance = Splat.objects.create(id=splat_obj.id, message=splat_obj.message)
        if splat_obj.painting:
            painting = Painting.objects.get(id=splat_obj.painting)
            splat_instance.painting = painting
            splat_instance.save()


class Migration(migrations.Migration):

    dependencies = [
        ('splat', '0004_auto_20150630_1356'),
    ]

    operations = [
        migrations.RunPython(load_splat_data),
    ]
