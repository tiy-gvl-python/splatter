# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import pandas as pd
from splat.models import Splatee


def load_splatee_data(apps, schema_editor):
    user_df = pd.read_csv('user_dataset.csv', names=["age", "sex", "occupation", "postal_code"])

    for row in user_df.iterrows():
        user_obj = row[1]
        Splatee.objects.create(age=user_obj.age, sex=user_obj.sex, occupation=user_obj.occupation, postal_code=user_obj.postal_code)


class Migration(migrations.Migration):

    dependencies = [
        ('splat', '0006_splatee'),
    ]

    operations = [
        migrations.RunPython(load_splatee_data)
    ]
