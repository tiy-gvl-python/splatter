# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models, migrations
from splat.models import Splatee

def create_users(x, b):
    for splatee in Splatee.objects.all():
        splatee.user = User.objects.create(username=str(splatee.id))
        splatee.user.set_password("asdf")
        splatee.user.save()
        splatee.save()


class Migration(migrations.Migration):

    dependencies = [
        ('splat', '0010_splatee_user'),
    ]

    operations = [
        migrations.RunPython(create_users)
    ]
