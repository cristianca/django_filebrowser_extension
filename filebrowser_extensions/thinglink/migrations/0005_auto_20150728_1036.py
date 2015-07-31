# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thinglink', '0004_auto_20150723_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thinglink',
            name='code',
            field=models.CharField(verbose_name='Code', help_text='Copy paste link to iframe here', unique=True, max_length=1000),
        ),
    ]
