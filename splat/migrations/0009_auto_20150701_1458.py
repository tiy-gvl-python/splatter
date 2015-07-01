# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import pandas as pd
from splat.models import Splat, Splatee

def load_splat_user_data(x, y):
    su_df = pd.read_csv('splat_user_dataset.csv', names=["splat", "user"])
    for su in su_df.iterrows():
        su_obj = su[1]
        splat = Splat.objects.get(id=su_obj.splat)
        splatee = Splatee.objects.get(id=su_obj.user)
        splat.splatee = splatee
        splat.save()



class Migration(migrations.Migration):

    dependencies = [
        ('splat', '0008_splat_splatee'),
    ]

    operations = [
        migrations.RunPython(load_splat_user_data)
    ]
