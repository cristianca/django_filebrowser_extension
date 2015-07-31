# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thinglink', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='thinglink',
            name='height',
            field=models.PositiveIntegerField(default=200),
        ),
        migrations.AddField(
            model_name='thinglink',
            name='width',
            field=models.PositiveIntegerField(default=200),
        ),
    ]
