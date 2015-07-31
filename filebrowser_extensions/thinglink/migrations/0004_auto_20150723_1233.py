# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thinglink', '0003_auto_20150722_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thinglink',
            name='code',
            field=models.CharField(max_length=1000, help_text='Copy paste link to iframe here', verbose_name='Code'),
        ),
    ]
